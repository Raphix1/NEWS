from django.shortcuts import render
from django.views import View
from .models import NewsCategory, News
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def get_category(request):
    return render(request, 'category.html')
