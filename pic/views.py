from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404
from .models import Image,Category,Location
# Create your views here.

def welcome(request):
    images = Image.objects.all()
    
    args={'images':images}
    return render(request,'all-fold/welcome.html',args)

def people (request):

    return render(request,'all-fold/people.html')