from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

import csv
import pandas as pd


def home(request):
    print('Strona główna')
    return render(request, 'home.html')


def my(request):
    print('O nas')
    return render(request, 'my.html')

def gramatyka(request):
    print('Gramatyka')
    return render(request, 'gramatyka.html')

def odmiana(request):
    print('Odmiana czasowników przez osoby')
    return render(request, 'odmiana.html')

def czasy(request):
    print('Czasy')
    return render(request, 'czasy.html')

def kontakt(request):
    print('Kontakt')
    return render(request, 'kontakt.html')

def rodzina(request):
    print('Rodzina')
    return render(request, 'rodzina.html')

def kolory(request):
    print('Kolory')
    return render(request, 'kolory.html')

def liczby(request):
    print('Liczby')
    return render(request, 'liczby.html')


def slowka(request):
    print('Nauka słówek')
    return render(request, 'slowka.html')


