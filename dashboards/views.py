from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from blogs.models import Category, BlogPost
from .forms import CategoryForm, PostForm

# Mixin personalizado para manejar mensajes
class MessageMixin:
    """
    Mixin para manejar mensajes de éxito en vistas basadas en clases.

    Attributes:
        success_message (str): Mensaje de éxito que se mostrará cuando se realice una operación exitosa.
        
    Methods:
        form_valid(form): Maneja la validación del formulario.
        delete(request, *args, **kwargs): Maneja la eliminación de un objeto.
    """
    success_message = ''
    
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.success_message:
            messages.success(self.request, self.success_message)
        return response

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if hasattr(self, 'success_message'):
            messages.success(request, self.success_message)
        return response


class DashboardView(LoginRequiredMixin, View):
    """
    Vista que muestra el dashboard del usuario.

    Attributes:
        login_url (str): URL de la página de login.
        template_name (str): Nombre del template que se utilizará para renderizar la vista.
        
    Methods:
        get(request): Maneja la solicitud GET.
    """
    login_url = 'login'
    template_name = 'dashboard/dashboard.html'
    
    def get(self, request):
        category_count = Category.objects.all().count()
        post_count = BlogPost.objects.filter(author=request.user).count()
        
        context = {
            'category_count': category_count,
            'post_count': post_count,
        }
        return render(request, self.template_name, context)

# Vistas basadas en clases para Categorías
class CategoryListView(LoginRequiredMixin, ListView):
    """
    Vista que muestra la Categoria al usuario

    
    """
    model = Category
    template_name = 'dashboard/categories/categories.html'
    context_object_name = 'categories'
    login_url = 'login'

class CategoryCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/categories/add_category.html'
    success_url = reverse_lazy('dashboard_categories')
    success_message = 'Categoría creada correctamente'
    login_url = 'login'

class CategoryUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/categories/edit_category.html'
    success_url = reverse_lazy('dashboard_categories')
    success_message = 'Categoría actualizada correctamente'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object()
        return context

class CategoryDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard_categories')
    success_message = 'Categoría eliminada correctamente'
    login_url = 'login'
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


# Vistas basadas en clases para Posts
class PostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'dashboard/posts/posts.html'
    context_object_name = 'posts'
    login_url = 'login'
    
    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)

class PostCreateView(LoginRequiredMixin, MessageMixin, CreateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'dashboard/posts/add_posts.html'
    success_url = reverse_lazy('dashboard_posts')
    success_message = 'Post creado correctamente'
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, MessageMixin, UpdateView):
    model = BlogPost
    form_class = PostForm
    template_name = 'dashboard/posts/edit_posts.html'
    success_url = reverse_lazy('dashboard_posts')
    success_message = 'Post actualizado correctamente'
    login_url = 'login'
    
    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context

class PostDeleteView(LoginRequiredMixin, MessageMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('dashboard_posts')
    success_message = 'Post eliminado correctamente'
    login_url = 'login'
    
    def get_queryset(self):
        return BlogPost.objects.filter(author=self.request.user)
        
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

# Vistas basadas en funciones (compatibilidad)
def dashboard(request):
    return DashboardView.as_view()(request)

def categories(request):
    return CategoryListView.as_view()(request)

def add_category(request):
    return CategoryCreateView.as_view()(request)

def edit_category(request, pk):
    return CategoryUpdateView.as_view()(request, pk=pk)

def delete_category(request, pk):
    return CategoryDeleteView.as_view()(request, pk=pk)

def posts(request):
    return PostListView.as_view()(request)

def add_post(request):
    return PostCreateView.as_view()(request)

def edit_post(request, pk):
    return PostUpdateView.as_view()(request, pk=pk)

def delete_post(request, pk):
    return PostDeleteView.as_view()(request, pk=pk)

