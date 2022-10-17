from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class CoffeeHouse(models.Model):
    SI = True
    NO = False
    
    YES_OR_NOT_CHOICES = [
      (SI,'Si'),
      (NO,'No'),
    ]
    
    name = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    wifi = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=SI)
    open_area = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=NO)
    silence_area = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=NO)
    vegan = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=NO)
    price_rate = models.IntegerField(default=0, null=True, blank=True, validators=[MaxValueValidator(3),MinValueValidator(1)])
    origen = models.CharField(max_length=255, null=True, blank=True)
    machine = models.CharField(max_length=255, null=True, blank=True)
    grinder = models.CharField(max_length=255, null=True, blank=True)
    barista = models.CharField(max_length=255, null=True, blank=True)
    schedule = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    coffee_image = models.ImageField(null=True, blank=True, upload_to="coffees_images/")
    stars_average = models.DecimalField(max_digits=2, decimal_places=1, default=0.5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering= ['-updated_at', '-created_at']
    
    def __str__(self):
        return self.name 
    
    
    
  
