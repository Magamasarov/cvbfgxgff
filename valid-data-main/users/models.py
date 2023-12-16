from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=20)
    price=models.DecimalField(decimal_places=2,max_digits=6)
    image=models.ImageField(blank=True, null=True)
