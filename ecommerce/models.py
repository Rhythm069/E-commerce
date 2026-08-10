from django.db import models
from django.contrib.auth.models import User

class Category(models.TextChoices):
    RINGS="Rings","Rings"
    NECKLACES="Necklaces","Necklaces"
    BRACELETS="Bracelets","Bracelets"
    EARRINGS="Earrings","Earrings"

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo= models.ImageField(upload_to='brands/', blank=True,null=True)
    description = models.TextField(blank =True, null=True)
    country = models.CharField(max_length=100, blank=True)

class Product(models.Model):
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="products",blank=True,null=True)
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    stock=models.BooleanField(default=True)
    image=models.ImageField(upload_to="products/",blank=True,null=True)
    size=models.CharField(max_length=100,blank=True,null=True)
    material=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=20,choices=Category.choices,default=Category.RINGS)

    def __str__(self):
        return self.name
class Customer(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(upload_to="profiles/",blank=True,null=True)
    phone_number=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)

class Cart(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="cart")
    created_at=models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product)
    count = models.IntegerField(default=1, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)



    def __str__(self):
        return self.name
