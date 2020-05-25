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