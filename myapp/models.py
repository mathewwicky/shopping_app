from django.db import models

# Create your models here.

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    desc = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to="images")
    
