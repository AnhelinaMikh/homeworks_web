from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Это главная страница")

def about(request):
    return HttpResponse("Это страница 'О нас'")

def contacts(request):
    return HttpResponse("Это страница с контактами")


