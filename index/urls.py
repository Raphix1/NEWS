from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/', views.get_category),
    path('news/', views.get_news),
]