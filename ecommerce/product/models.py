from django.db import models
import datetime
from user.models import User 
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name 
  
  
  
class ProductAbstract(models.Model):
    name = models.CharField(max_length=50) 
    stock = models.IntegerField()
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/product/" + str(datetime.datetime.now()) + "/" )
    price = models.IntegerField()
    
    class Meta:
        abstract = True    
    
class Product(ProductAbstract):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    # name = models.CharField(max_length=50) 
    # stock = models.IntegerField()
    # description = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="images/product/" + str(datetime.datetime.now()) + "/" )
    # price = models.IntegerField()
    
    def __str__(self):
        return self.name 
    
class ProductProperty(ProductAbstract): 
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, )   
    # color = models.CharField(max_length=50)
    # image = models.ImageField(upload_to="images/product/" + str(datetime.datetime.now()) + "/" )
    rating = models.IntegerField()
    
    
    def __str__(self):
        return self.product_name.name
    
    
class Cart(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, )   
    product_property =  models.ForeignKey(ProductProperty, on_delete=models.CASCADE, )  
    
    def __str__(self):
        return self.user.name
    
     
    
        