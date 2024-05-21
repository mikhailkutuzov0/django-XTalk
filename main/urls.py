from django.urls import path
from . import views

app_name = 'main'  # Пространство имен для URL-адресов

urlpatterns = [
    path('', views.home, name='home'),

]
