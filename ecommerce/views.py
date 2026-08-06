
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
def home(request):
    details={
        "customer_name":"John Doe",
        "product_count":12,
    }
    return render(request, "ecommerce/index.html",details)

def about(request):
    return render(request,"ecommerce/about.html")

def contact(request):
    return render(request,"ecommerce/contact.html")

def collection(request):
    products=Product.objects.all()
    
    return render(request,"ecommerce/collection.html",{"products": products})


