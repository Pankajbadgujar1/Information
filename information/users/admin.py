from django.contrib import admin
from .models import Teachers
# Register your models here.

#super user created username : pankaj password : pass
@admin.register(Teachers)

class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'T_name', 'Designation', 'Username', 'Pass_word', 'Mobile_number', 'Email', 'DOB', 'Date_of_Joining']



