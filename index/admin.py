from django.contrib import admin
from .models import NewsCategory, News

# Register your models here.
@admin.register(NewsCategory)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['head']


