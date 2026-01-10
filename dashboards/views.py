from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, BlogPost
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm
from django.contrib import messages


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    post_count = BlogPost.objects.filter(author=request.user).count()

    context = {
        'category_count': category_count,
        'post_count': post_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories/categories.html')


@login_required(login_url='login')
def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente')
            return redirect('dashboard_categories')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/categories/add_category.html', context)


@login_required(login_url='login')
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada correctamente')
            return redirect('dashboard_categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'dashboard/categories/edit_category.html', context)


@login_required(login_url='login')
def delete_category(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('dashboard_categories')


@login_required(login_url='login')
def posts(request):
    posts = BlogPost.objects.filter(author=request.user)

    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts/posts.html', context)


@login_required(login_url='login')
def add_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado correctamente')
            return redirect('dashboard_posts')
        else:
            print(form.errors)
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/posts/add_posts.html', context)


@login_required(login_url='login')
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post actualizado correctamente')
            return redirect('dashboard_posts')
        else:
            print(form.errors)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'dashboard/posts/edit_posts.html', context)


@login_required(login_url='login')
def delete_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    post.delete()
    return redirect('dashboard_posts')

