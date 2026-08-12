from django.urls import path
from .views import (HelloAPIView, ProductListAPIView,CategoryDetailAPIView,BrandDetailsAPIView)

urlpatterns =[
    path('hello/',HelloAPIView.as_view(), name='hello'),
    path('product/',ProductListAPIView.as_view(), name='product-list'),
    path('categorys/',CategoryDetailAPIView.as_view(),name='category-details'),
    path('brands/',BrandDetailsAPIView.as_view(),name='brand-detail'),
    path('brands/<int:pk>',BrandDetailsAPIView.as_view(),name='brand-list')

]   

