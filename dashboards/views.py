from django.shortcuts import render, redirect
from blogs.models import Category, BlogPost
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    post_count = BlogPost.objects.all().count()

    context = {
        'category_count': category_count,
        'post_count': post_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')

@login_required(login_url='login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_categories')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

@login_required(login_url='login')
def edit_category(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard_categories')

    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('dashboard_categories')


@login_required(login_url='login')
def posts(request):
    posts = BlogPost.objects.all()

    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts/posts.html', context)

@login_required(login_url='login')
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_posts')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/posts/add_posts.html', context)
