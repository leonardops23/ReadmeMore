from django.contrib import admin
from .models import Category, BlogPost

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model.
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        prepopulated_fields (dict): Fields to auto-populate based on other fields.
        search_fields (tuple): Fields to include in the search functionality.
        ordering (tuple): Default ordering of the categories in the admin interface.
    """
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)

class BlogPostAdmin(admin.ModelAdmin):
    """
    Admin interface for BlogPost model.
    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        prepopulated_fields (dict): Fields to auto-populate based on other fields.
        list_filter (tuple): Fields to filter the list view.
        search_fields (tuple): Fields to include in the search functionality.
        ordering (tuple): Default ordering of the blog posts in the admin interface.
    """
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'is_featured', 'category')
    list_editable = ('is_featured',)
    search_fields = ('title', 'content', 'author__username')
    ordering = ('-created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
