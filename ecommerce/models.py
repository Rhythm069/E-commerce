from django.db import models

class Category(models.TextChoices):
    Rings = "Rings","Rings"
    Necklaces = "Necklacs","Necklacs"
    Bracelets = "Bracelets","Bracelets"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00,blank=True,null=True)
    description = models.TextField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/',blank=True,null=True)



    def _str_(self):
        return self.name


# Create your models here.
