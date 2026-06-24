from django.db import models

# Create your models here.
class Food(models.Model):
    name= models.CharField(max_length=100, unique=True)
    calories_per_gram=models.FloatField()



    def __str__(self):
        return self.name