from django.shortcuts import redirect, render
from blogs.models import Category, BlogPost
from assignments.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }

    return render(request, 'login.html', context)


def logout_view(request):
    auth.logout(request)
    return redirect('home')
