from django.http import HttpResponse
from django.shortcuts import render

# komandy
# django-admin startproject myproject - sozdajot proekt
# python manage.py migrate - migracija proekta
# python manage.py runserver - zapusk proekta


def startovaja(request):
    return HttpResponse('Poluchilos')

def home(request):
    return render(request, 'home.html', {'greeting': 'Hallo!'})