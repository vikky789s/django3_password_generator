from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #return HttpResponse( 'Hello there friend!')
    #return render (request, 'generator/home.html', {'password':'hui43g6i527u'})
    return render (request, 'generator/home.html')

def password(request):
    #return HttpResponse('<h1>Eggs are tasty and whte egg is good for health<h1>')

    characters = list('abcdefghijklmnopqrstuvwxyz')
    #"""
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('Numbers'):
        characters.extend(list('0123456789'))
         
    if request.GET.get('Specialcharacters'):
        characters.extend(list("`~!@#$%^&*()_+=|/?><.,"))

    length = int(request.GET.get('length', 12))
    
    #length = 12
    thepassword = ''
    
    for x in range (length):
        thepassword += random.choice(characters) 

    return render (request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render (request, 'generator/about.html')