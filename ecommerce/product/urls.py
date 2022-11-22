

from django.urls import path
from .views import  dashboard, show_product, add_cart, show_cart, remove_item, order_item, show_order_item



urlpatterns = [
    path('dashboard/',  dashboard, name= "dashboard"),
    path('show_product/<int:id>/',  show_product, name= "show_product"),
    path('add_cart/<int:id>/<int:show_product_id>',  add_cart, name= "add_cart"),
    path('show_cart/',  show_cart, name= "show_cart"),
    path('remove_item/<int:id>/', remove_item, name= "remove_item"),
    path('order_item/<int:amount>/', order_item, name= "order_item"),
    path('show_order_item/', show_order_item, name= "show_order_item"),

]