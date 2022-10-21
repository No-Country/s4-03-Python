from django.db import models

# Create your models here.
class TitleMessage(models.Model):
    SI = True
    NO = False
    
    YES_OR_NOT_CHOICES = [
      (SI,'Si'),
      (NO,'No'),
    ]
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=20, null=True)
    is_active = models.BooleanField(choices=YES_OR_NOT_CHOICES, default=NO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)                                  
    
    def __str__(self) -> str:
        return self.slug                                  

  