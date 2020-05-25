from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location
# Create your views here.

def welcome(request):
    
    return render(request,'all-fold/welcome.html')

def people (request):

    return render(request,'all-fold/people.html')
def travel (request):

    context={
        'images':Image.objects.all()
        }
    return render(request,'all-fold/travel.html',context)

   

# def search_results(request):
#     if 'image' in request.GET and request.GET["image"]:
#         search_term = request.GET.get("image")
#         searched_images= Image.search_by_category(search_term)

#         message = f"{search_term}"


#         return render(request, 'all-fold/search.html',{"message":message,"images":searched_images})


#     else:
#         message = "You haven't searched for any term"

#         return render(request,'all-fold/search.html',{"message":message})




# def photo (request):
#     images=Image.objects.filter(category="PHOTO")

#     args={'images':images}
#     return render(request,'all-fold/travel.html',args)


# def food (request):
#     images=Image.objects.filter(category="FOOD")
#     args={'images':images}
#     return render(request,'all-fold/travel.html',args)

# def personal (request):
#     images=Image.objects.filter(category="3")
#     args={'images':images}
#     return render(request,'all-fold/travel.html',args)

# @classmethod
# def search_image(cls, search_term):
#     images = cls.objects.filter(category__category=search_term)
#     return images
