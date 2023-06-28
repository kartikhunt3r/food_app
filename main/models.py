from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=255)
    # location = models.CharField(max_length=255)
    # itemzs = models.CharField(max_length=255)
  

    def __str__(self):
        return self.name

class Dishz(models.Model):
    name = models.CharField(max_length=25500)
    location = models.CharField(max_length=25500)
    items = models.CharField(max_length=255000)
  

    def __str__(self):
        return self.name,self.location,self.items
