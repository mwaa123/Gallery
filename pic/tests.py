from django.test import TestCase
from .models import Image,Location,Category


class ImageTestClass(TestCase):

    def setUp(self):
        self.photoshoot= Image(name = 'photoshoot', description ='sunset photo')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.photoshoot,Image))

    def test_save_method(self):
        self.photoshoot.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    # def test_updated_image(self):
    #     update=Image.update_image(self.image1.image_name,'Updated Test')
    #     self.assertEqual(update.image_name,'Updated Test')
     
     # Detlete image   
    def test_delete_image(self):
        Image.delete_image(self)
        self.assertTrue(len(Image.objects.all())==0)
        
    #Get image by id
    # def test_get_image_by_id(self):
    #     image=Image.get_image_by_id(self.id)
    #     self.assertTrue(len(image)==1)
        
    #Seach by category
        image=Image.search_image(self.category.category)
        self.assertTrue(len(image)>0)    


# tTest for category
class CategoryTestClass(TestCase):


    def setUp(self):
        self.food= Category(category = 'food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

    
    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)


    @classmethod
    def update_category(cls,name,update):
        Category.objects.filter(category=name).update(category=update)
        update=Category.objects.get(category=update)
        return update   

    def test_delete_category(self):
        Category.delete_category(self.category.category)
        self.assertTrue(len(Category.objects.all())==0)





class TestLocation(TestCase):
    def setUp(self):
        self.location=Location(location='nairobi')
        self.location.save_location()
    
    def tearDown(self):
        Location.objects.all().delete()
            
    def test_location_save(self):
        self.location.save_location()
        
    def test_update_location(self):
        update=Location.update_location(self.location.location,'nairobi')
        self.assertEqual(update.location,'nairobi')
        
    def test_delete_location(self):
        delete=Location.delete_location(self.location)
        self.assertTrue(len(Location.objects.all())==0)      