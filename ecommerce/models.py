from django.db import models

class Product(models.Model):

    class Category(models.TextChoices):
        RINGS = "Rings", "Rings"
        NECKLACES = "Necklaces", "Necklaces"
        BRACELETS = "Bracelets", "Bracelets"

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.RINGS
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo= models.ImageField(upload_to='brands/', blank=True,null=True)
    description = models.TextField(blank =True, null=True)
    country = models.CharField(max_length=100, blank=True)

class Customer(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product = models.ManyToManyField(Product)
    count = models.IntegerField(default=1, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.name
