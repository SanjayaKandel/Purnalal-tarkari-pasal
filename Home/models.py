from django.db import models

# Create your models here.
class vegetable(models.Model):
    name = models.CharField(max_length = 15)
    quantity = models.IntegerField()
    price =models.IntegerField()

    def __str__(self):
        return self.name

class fruit(models.Model):
    name = models.CharField(max_length = 15)
    quantity = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
         return self.fname

