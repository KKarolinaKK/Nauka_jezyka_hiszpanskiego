from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

import csv
import pandas as pd

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'notatka.html', {'form': form})

def home(request):
    print('Strona główna')
    return render(request, 'home.html')

def notatka(request):
    print('Twoje notatki')
    return render(request, 'notatka.html')

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

def notatka(request):
    print('Twoje notatki')
    return render(request, 'notatka.html')

def liczby(request):
    print('Liczby')
    return render(request, 'liczby.html')

def gustar(request):
    print('Co lubię?')
    return render(request, 'gustar.html')

def slowka(request):
    print('Nauka słówek')
    return render(request, 'slowka.html')

def hola(request):
    print('Przywitaj sie i powiedz coś o sobie')
    return render(request, 'hola.html')

