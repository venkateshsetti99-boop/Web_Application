from django.contrib import admin
from .category import Category
from .product import Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'cat', 'created_at']
    list_filter = ['cat']
    search_fields = ['name', 'desc']
