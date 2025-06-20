from django.contrib import admin
from .models import Category, Product
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  """Custom model category admin"""
  prepopulated_fields = {'slug': ('name',)} #Auto fill fileds (before) base difference fields
  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  """Custom model category admin"""
  prepopulated_fields = {'slug': ('title',)} #Auto fill fileds (before) base difference fields
  
