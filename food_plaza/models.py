from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class user_reg(models.Model):
	#userid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=14)
    address=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
   
    
    
    def __str__(self):
        return self.name



class recipe_table(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_type=models.CharField(max_length=100)
    ingredient=models.CharField(max_length=1000)
    description=models.CharField(max_length=1000)
    process_of_making=models.CharField(max_length=2000)
    picture=models.ImageField(upload_to="recipe/images")
 
    def __str__(self):
        return self.recipe_name


    


