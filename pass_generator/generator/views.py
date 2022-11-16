from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenth = 10

    for i in range(lenth):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
