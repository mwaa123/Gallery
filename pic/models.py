from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    category_image = models.ImageField(upload_to = 'image/', blank=True)

class Category(models.Model):
    name = models.CharField(max_length =30)
    
    