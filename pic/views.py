from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404

# Create your views here.

def welcome(request):

    return render(request,'all-fold/welcome.html')

def people(request):

    return render(request,'all-fold/people.html')