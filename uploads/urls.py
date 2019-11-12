from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('slowka/', views.slowka, name='slowka'),
    url('my/', views.my, name='my'),
    url('kontakt/', views.kontakt, name='kontakt'),
]
