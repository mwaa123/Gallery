from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length =30, blank=True)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


     #UPdate Category
    @classmethod
    def update_category(cls,name,update):
        Category.objects.filter(category=name).update(category=update)
        update=Category.objects.get(category=update)
        return update   
    # delete category

    @classmethod    
    def delete_category(cls,category):
        Category.objects.get(category=category).delete()
    

        
class Location(models.Model):
    location = models.CharField(max_length =30 ,null=True) 

    def __str__(self):
        return self.location

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'blog/', blank=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE ,null=True )
    location = models.ForeignKey('Location',on_delete=models.CASCADE ,null=True )
    @classmethod
    def search_by_category(cls,search_term):
        fine = cls.objects.filter(category__category__icontains=search_term)
        return fine
    
    
    
    def __str__(self):
        return self.name


    def save_image(self):
        self.save()

# @classmethod
# def search_image(cls, search_term):
#     images = cls.objects.filter(category__category__icontains=search_term)
#     return images


#  @classmethod
#     def search_image(cls,category):
#         image=cls.objects.get(category=category)
#         return image
        
#     @classmethod
#     def filter_by_location(cls,location):
#         image=Image.objects.get(location=location)
#         return image






















# @classmethod
# def search_by_location(cls, search_term):
#      images = cls.objects.filter(location__place=search_term)
#      return images 




