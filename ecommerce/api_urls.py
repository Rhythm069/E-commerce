from django.urls import path
from .views import (HelloAPIView, ProductListAPIView)

urlpatterns =[
    path('hello/',HelloAPIView.as_view(), name='hello'),
    path('product/',ProductListAPIView.as_view(), name='product-listt')
]   