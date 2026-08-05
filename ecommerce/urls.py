from django.urls import path
from . import views
app_name = "ecommerce"
urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about, name ='about'),
    path('contact/',views.contact, name ='contact'),
    path('collection/',views.collection, name ='collection')

]