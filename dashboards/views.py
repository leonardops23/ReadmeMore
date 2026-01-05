from django.shortcuts import render
from blogs.models import Category, BlogPost
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.count()
    post_count = BlogPost.objects.count()

    context = {
        'category_count': category_count,
        'post_count': post_count,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def categories(request):
    return render(request, 'dashboard/categories.html')
