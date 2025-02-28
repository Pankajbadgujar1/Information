from django.core.mail import send_mail
from django.conf import settings

def send_approval_email(user):
    subject = 'Your Account has been Approved'
    message = f'Hello {user.username},\n\nYour account has been approved. You can now log in.\n\nUsername: {user.username}\nPassword: [Your Chosen Password]'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
# Compare this snippet from information/users/models.py:
# from django.db import models