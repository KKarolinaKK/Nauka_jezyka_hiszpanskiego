from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('slowka/', views.slowka, name='slowka'),
    url('my/', views.my, name='my'),
    url('kontakt/', views.kontakt, name='kontakt'),
    url('rodzina/', views.rodzina, name='rodzina'),
    url('kolory/', views.kolory, name='kolory'),
    url('liczby/', views.liczby, name='liczby'),
    url('gramatyka/', views.gramatyka, name='gramatyka'),
    url('czasy/', views.czasy, name='czasy'),
    url('odmiana/', views.odmiana, name='odmiana'),
    url('notatka/', views.notatka, name='notatka'),
    url('gustar/', views.gustar, name='gustar'),
    url('hobby/', views.hobby, name='hobby'),
    url('hola/', views.hola, name='hola')
]
