from django.shortcuts import render
from product.models import Product, ProductProperty, Cart,Order 
from user.models import User
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.




def dashboard(request):
     context = { 'title' : "Dashboard",
                'products': Product.objects.all() }
     return render(request, 'product/dashboard.html', context=context)

def show_product(request, id=None):
     if id is not None: 
          context = { 'title' : "Show Product",
                    'show_products_property': ProductProperty.objects.filter(product_name__id=id),
                    'show_product_id':id 
                    }
          return render(request, 'product/show_product.html', context=context)          


def add_cart(request, id=None, show_product_id=None):
     if id is not None: 
          product_property_instance = ProductProperty.objects.get(id=id)
          # product_instance = product_property_instance.product_name 
          user_instance = User.objects.get(email=request.user)
          user = Cart(user=user_instance, product_property=product_property_instance)
          user.save()
          return  HttpResponseRedirect(reverse('show_product', kwargs={"id": show_product_id}))

def show_cart(request):
     user_instance = User.objects.get(email=request.user)
     cart_queryset = Cart.objects.filter(user=user_instance, is_not_order=True)
     total_price = 0 
     for instance in cart_queryset:
          total_price += instance.product_property.price 
     context = { 'title' : "Show Cart", 
                 'cart_queryset' : cart_queryset,
                 'total_price': total_price
               }
     return render(request, 'product/show_cart.html', context=context)
 
def remove_item(request, id=None):
     if id is not None:
          remove_data = Cart.objects.get(id=id)
          remove_data.delete()
          return  HttpResponseRedirect(reverse('show_cart'))


def order_item(request, amount=None):
     if amount is not None:
          user_instance = User.objects.get(email=request.user)
          cart_queryset = Cart.objects.filter(user=user_instance)
          
          for instance in cart_queryset:
               if instance.is_not_order:
                    order_item = Order(user=user_instance, order_item=instance, amount=amount)
                    order_item.save()
                    instance.is_not_order = False 
                    instance.save() 

          # cart_item_empty = Cart.objects.all()
          # cart_item_empty.delete() 
          return  HttpResponseRedirect(reverse('show_cart'))
          
          
def show_order_item(request):

     user_instance = User.objects.get(email=request.user)
     order_item_queryset = Order.objects.filter(user=user_instance, is_receive_product=False)
     context = { 'title' : 'Order Item',
                'order_item_queryset': order_item_queryset, 
               }
     return render(request, 'product/show_order_item.html', context=context)
               

     

     