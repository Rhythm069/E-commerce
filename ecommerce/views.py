
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .forms import ContactForm
from .forms import FeedbackForm
def home(request):
    details={
        "customer_name":"John Doe",
        "product_count":12,
    }
    return render(request, "ecommerce/index.html",details)

def about(request):
    Form=FeedbackForm
    return render(request,"ecommerce/about.html",{'Form':FeedbackForm})

def contact(request):
    Form=ContactForm()
    return render(request,"ecommerce/contact.html",{'Form':ContactForm})

def collection(request):
    products=Product.objects.all()
    
    return render(request,"ecommerce/collection.html",{"products": products})


