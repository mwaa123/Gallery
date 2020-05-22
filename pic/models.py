from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog', blank=True)

    def save_image(self):
        self.save()

    # def delete_image(self):
    #     self.delete() 

class Category(models.Model):
    name = models.CharField(max_length =30)
    image = models.ForeignKey(Image)

    # def save_category(self):
    #     self.save()



class Location(models.Model):
    place = models.CharField(max_length =30)