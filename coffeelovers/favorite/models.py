from django.db import models
from coffee_house.models import CoffeeHouse
from django.contrib.auth.models import User
from django.utils import timezone

class Favorite(models.Model):
    SI = True
    NO = False
    
    YES_OR_NOT_CHOICES = [
      (SI,'Si'),
      (NO,'No'),
    ]
    house = models.ForeignKey(CoffeeHouse, on_delete=models.CASCADE, null=True, to_field='id')
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=SI)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return "Favorites: "+ str(self.house) 
    