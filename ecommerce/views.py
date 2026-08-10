
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.shortcuts import render,redirect
from .models import Product
from .forms import ContactForm
from .forms import FeedbackForm
from .forms import LoginForm

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
    Form=ContactForm
    return render(request,"ecommerce/contact.html",{'Form':ContactForm})

def collection(request):
    products=Product.objects.all()
    
    return render(request,"ecommerce/collection.html",{"products": products})


def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("ecommerce:home")

        else:
            error_message = "Invalid username or password. Please try again."

            return render(
                request,
                "ecommerce/login.html",
                {
                    "Form": LoginForm(),
                    "error_message": error_message
                }
            )

    # This is for GET /login/
    return render(
        request,
        "ecommerce/login.html",
        {
            "Form": LoginForm()
        }
    )
def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:login')
      
    return render(request,"ecommerce/register.html",{'form':form})


@login_required
def profile(request):
    return render(request,"ecommerce/profile.html")

@login_required
def cart(request):
    return render(request,"ecommerce/cart.html")

def logout(request):
    auth_logout(request)
    return redirect('ecommerce:home')