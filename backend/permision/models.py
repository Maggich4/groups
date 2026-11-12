from django.db import models
from django.contrib.auth.models import AbstractUser, User

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
            return self.title
        
class CustomUser(AbstractUser):
    
    phone = models.CharField(max_length=20, blank=True)
    birth_data = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username