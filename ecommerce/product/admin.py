from django.contrib import admin
from .models import Product, Category, ProductProperty, Cart
# Register your models here.



@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',) 
@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'rating', 'name', 'stock', 'description', 'image', 'price') 



@admin.register(ProductProperty)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'name', 'rating', 'stock', 'description', 'image', 'price', 'rating') 



@admin.register(Cart)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_name', 'product_property') 


