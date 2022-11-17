from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenth = int(request.GET.get('length', 10))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specialCharacter'):
        characters.extend(list('!@#$%^&*()_+'))

    for i in range(lenth):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
