from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/', views.get_category),
    path('news/', views.get_news),
    path('search', views.search_news),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
]