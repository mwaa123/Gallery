from django.test import TestCase
from .models import Image,Location,Category

# test for the image class.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photoshoot= Image(name = 'photoshoot', description ='sunset photo')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photoshoot,Image))
    # Testing Save Method
    def test_save_method(self):
        self.photoshoot.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # def test_delete_method(self):
    #     self.photoshoot.delete_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images) > 0)



# tTest for category
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.food= Category(name = 'food')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))


    # def test_save_method(self):
    #     self.food.save_category()
    #     categories = Category.objects.all()
    #     self.assertTrue(len(categories) > 0)
