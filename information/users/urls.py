
from django.urls import path
from users import views

urlpatterns = [
    path('', views.homePage, name='HomePage'),

    path('Teacher_login/', views.Teacher_login, name = 'Teacher_login'),
    path('dashboard/', views.dashboard, name = 'Dashboard'),

    
]
