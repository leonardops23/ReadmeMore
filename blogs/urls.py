from django.urls import path, include
from .views import posts_by_category, post_detail

urlpatterns = [
    path('<int:category_id>/', posts_by_category, name='posts_by_category'),
]
