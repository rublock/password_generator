from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')

def password(request):

    thepassword = 'testing'

    return render(request, 'generator/password.html', {'password': thepassword})
