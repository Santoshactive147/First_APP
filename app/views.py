from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {"Name":"Santosh"}
    return render(request,"index.html",context)
    

def try1(request):
    
    return render(request,"try1.html",{"word":"This is from app templates"})