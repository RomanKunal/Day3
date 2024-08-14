from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataFromDB, name='dataFromDB'),
]