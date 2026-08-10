from django.urls import path
from . import views
app_name = "ecommerce"
urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about, name ='about'),
    path('contact/',views.contact, name ='contact'),
    path('collection/',views.collection, name ='collection'),
    path('login/',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('cart/',views.profile, name='cart'),
    path('logout/', views.logout, name='logout'),
    



]