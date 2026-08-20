
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render,redirect
from .models import Product,Category,Brand
from .forms import ContactForm,LoginForm, FeedbackForm
from .serializers import ProductSerializer,CategorySerializer,BrandSerializer
from rest_framework import generics, mixins



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


class HelloAPIView(mixins.ListModelMixin,mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self,request, *args, **kwargs):
        return self.partial_update(request, *args ,**kwargs)

    def patch(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



    
class ProductListAPIView(APIView):
    def get(self ,request):                                                
        products=Product.objects.all()
        serializer=ProductSerializer(
            products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class BrandDetailsAPIView(APIView):
    def get(self, request):
        brands = Brand.object.all()
        serializer=BrandSerializer(brands, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        brands=Brand.objects.get(pk=pk)
        serializer = BrandSerializer(brands, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)







