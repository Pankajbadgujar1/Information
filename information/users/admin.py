from django.contrib import admin

from users.utils import send_approval_email
from .models import Teachers, customUser

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_approved']
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        for user in queryset:
            user.is_approved = True
            user.active = True
            user.save()
            send_approval_email(user)

    approve_users.short_description = 'Approve selected users'
admin.site.register(customUser, CustomUserAdmin)


#super user created username : pankaj password : pass
@admin.register(Teachers)

class TeacherAdmin(admin.ModelAdmin):
    list_display = [ 'T_name', 'Designation', 'Username', 'Pass_word', 'Mobile_number', 'Email', 'DOB', 'Date_of_Joining']



