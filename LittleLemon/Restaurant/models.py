from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self): 
        return self.name

class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   inventory = models.IntegerField() 

   def __str__(self):
      return self.title