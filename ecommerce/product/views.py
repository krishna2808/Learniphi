from django.shortcuts import render
from product.models import Product

# Create your views here.




def dashboard(request):
     context = {'products': Product.objects.all() }
     return render(request, 'product/dashboard.html', context=context)