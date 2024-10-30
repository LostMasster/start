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

def some_page(request):
    usertext = request.GET['user_text']
    reversed_text = usertext[::-1]
    number_of_words = len(usertext.split())
    return render(request, 'some_page.html',
                  {'user_text': usertext, 'reversedtext': reversed_text,
                   'number_words': number_of_words})
