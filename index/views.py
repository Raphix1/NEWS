from django.shortcuts import render
from django.views import View
from .models import NewsCategory, News
# Create your views here.
def home_page(request):
    view_news = News.objects.all()
    view_categ = NewsCategory.objects.all()

    context = {'view_news': view_news,
               'view_categ': view_categ}
    return render(request, 'home.html', context)

def get_category(request):
    return render(request, 'category.html')

def get_news(request):
    return render(request, 'news.html')