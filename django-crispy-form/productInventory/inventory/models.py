from django.db import models

# Create your models here.
class Product(models.Model):
    # Create an auto-incremented db table field
    product_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=100)

    # Optionally, we need to enable a string representation of this 
    # class, so we can easily display the product name
    def __str__(self):
        return self.name
