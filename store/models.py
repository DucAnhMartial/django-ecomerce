from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255,db_index=True)
  slug = models.SlugField(max_length=255, unique=True)
  
  
  class Meta:
    verbose_name = 'category' #Hiển thị dạng số ít
    verbose_name_plural = 'categories'  #Hiển thị dạng số nhiều 
    
  #Thể hiện chuỗi đại diện cho models 
  def __str__(self):
    return self.name
  
  
class Product(models.Model):
  title = models.CharField(max_length=250)
  brand = models.CharField(max_length=255, default='un-branded')
  description = models.TextField(blank=True)
  slug = models.SlugField(max_length=255)
  pirce = models.DecimalField(max_digits=4, decimal_places=2)
  image = models.ImageField(upload_to='images/')
  
  class Meta:
    verbose_name = 'product' #display singular form
    verbose_name_plural = 'products'  #display plural form
    
   #add image field
   
    
    
  #Thể hiện chuỗi đại diện cho models 
  def __str__(self):
    return self.title
  