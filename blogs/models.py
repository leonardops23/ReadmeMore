from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    """
    Model representing a blog category.

    Attributes:
        name (str): The name of the category.
        slug (str): A URL-friendly version of the category name.
        available (bool): Availability status of the category.
        created_at (datetime): Timestamp when the category was created.
        updated_at (datetime): Timestamp when the category was last updated.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwars):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwars)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the blog post.
        slug (str): A URL-friendly version of the blog post title.
        author (User): The author of the blog post.
        short_content (str): A brief summary of the blog post.
        content (str): The main content of the blog post.
        featured_image (Image): An optional featured image for the blog post.
        category (Category): The category to which the blog post belongs.
        status (str): The publication status of the blog post (draft or published).
        is_featured (bool): Whether the blog post is featured.
        created_at (datetime): Timestamp when the blog post was created.
        updated_at (datetime): Timestamp when the blog post was last updated.
    """
    class Choices(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    short_content = models.TextField(max_length=300, blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=2, choices=Choices.choices, default=Choices.DRAFT)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

