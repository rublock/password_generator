from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('specialCharacter'):
        characters.extend(list('!@#$%^&*()_+'))

    lenth = int(request.GET.get('length', 10))

    for i in range(lenth):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    params = request.GET.get('?', '')
    # print(params)
    return render(request, 'generator/about.html')
