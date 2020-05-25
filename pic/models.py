from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length =30, blank=True)

    def __str__(self):
        return self.category
    # save category
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


    def save_location(self):
        self.save()
     #Update location
    @classmethod
    def update_location(cls,name,update):
        Location.objects.filter(location=name).update(location=update)  
        updated=Location.objects.get(location=update)
        return updated

        
    #Delete location    
    @classmethod    
    def delete_location(cls,location):
        deleted=Location.objects.get(location=location).delete()
        return deleted     

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
     #UPDATE IMAGE
    # @classmethod
    # def update_image(cls,name,update):
    #     Image.objects.filter(image_name=name).update(image_name=update)
    #     update=Image.objects.get(image_name=update)
    #     return update    
        
    #DELETE IMAGE    
    @classmethod    
    def delete_image(cls,image):
        Image.objects.get(image_name=image).delete()
        
    #GET IMAGE BY ID
    # @classmethod
    # def get_image_by_id(cls,id):
    #     image=Image.objects.filter(id=id)
    #     return image
        
    @classmethod
    def search_results(cls,category_image):
        categories=Category.objects.filter(category=category_image)
        for category in categories:          
            image=cls.objects.filter(category=category)
        return image
    
























