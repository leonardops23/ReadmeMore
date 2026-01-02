from django.shortcuts import render
from blogs.models import Category

def home(request):
    categories = Category.objects.filter(available=True).order_by('name')
    
    context = {
        'categories': categories
    }
    return render(request, 'home-blogs.html', context)

