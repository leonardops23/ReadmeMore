from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard_index'),
    path('categories/', views.categories, name='dashboard_categories'),
]
