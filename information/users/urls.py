from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    
    path('Teacher_login/', views.Teacher_login, name = 'Teacher_login'),
    path('homepage/', views.homePage, name='HomePage'),

    
]
