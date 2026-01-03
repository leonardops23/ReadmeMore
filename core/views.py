from django.shortcuts import render
from blogs.models import Category, BlogPost
from assignments.models import About


def home(request):
    featured_blogs = BlogPost.objects.filter(is_featured=True, status=BlogPost.Choices.PUBLISHED).order_by('-created_at')[:3]
    posts = BlogPost.objects.filter(is_featured=False, status=BlogPost.Choices.PUBLISHED).order_by('-created_at')[:6]

    try:
        about = About.objects.latest('created_at')
    except About.DoesNotExist:
        about = None

    context = {
        'featured_blogs': featured_blogs,
        'posts': posts,
        'about': about,
    }

    return render(request, 'home-blogs.html', context)
