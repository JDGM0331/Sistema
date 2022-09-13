from unicodedata import name
from django.urls import path

from Libreria.views import nosotros
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
]   