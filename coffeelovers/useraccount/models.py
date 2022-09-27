from django.db import models
from django.contrib.auth.models import AbsatractUser

# Create your models here.
class User(AbsatractUser):
    is_email_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.email

