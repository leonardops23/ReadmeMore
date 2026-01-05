from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category, BlogPost
from django.db.models import Q


def posts_by_category(request, category_id):
    posts = BlogPost.objects.filter(status=BlogPost.Choices.PUBLISHED, category=category_id)
    category = get_object_or_404(Category, id=category_id)
    # try:
    #     category = Category.objects.get(id=category_id)
    # except Category.DoesNotExist:
    #     return redirect('home')
    # category = Category.objects.get(id=category_id)

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'blogs/posts_by_category.html', context)


def post_detail(request, slug):
    single_blog = get_object_or_404(BlogPost, slug=slug, status=BlogPost.Choices.PUBLISHED)

    context = {
        'single_blog': single_blog,
    }

    return render(request, 'dashboard/post.html', context)


def search_posts(request):
    # estamos completamos la parte de busqueda.
    keyword = request.GET.get('keyword')
    result = BlogPost.objects.all()
    print(f"keyword: {keyword}")
    if keyword:
        result = result.filter(
            Q(title__icontains=keyword) |
            Q(short_content__icontains=keyword) |
            Q(content__icontains=keyword),
            status=BlogPost.Choices.PUBLISHED,
        )

    context = {
        'keyword': keyword,
        'result': result,
    }

    return render(request, 'blogs/search_results.html', context)

