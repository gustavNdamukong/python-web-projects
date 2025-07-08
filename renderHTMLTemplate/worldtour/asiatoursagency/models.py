from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need an origin country, we need a destination, number of nights, and 
    # we need a price for that tour
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.CharField() 

    # This is a magic method to create a string representation of the tours. 
    # It will allow you to be able to print out the structure of this model 
    # class into a string, by using something like the stir() method
    # another magic function which can achieve the same thing is __repr__()
    def __str__(self):
        return (
            f"ID:{self.id}: From {self.origin_country} To {self.destination_country}," 
            f"{self.number_of_nights} nights costs ${self.price}"
        )