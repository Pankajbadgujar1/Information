from django.db import models

from django.contrib.auth.hashers import make_password, check_password   

# Create your models here.

class Teachers(models.Model):
    T_name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Username = models.CharField(max_length=50)
    Pass_word = models.CharField(max_length=50)
    Mobile_number =models.CharField(max_length=10)
    Email = models.EmailField()
    DOB = models.DateField()
    Date_of_Joining = models.DateField()


    def save(self, *args, **kwargs):
        """ Hash password before saving if it's not already hashed """
        if not self.Pass_word.startswith('pbkdf2_sha256$'):  # ✅ Prevent rehashing already hashed passwords
            self.Pass_word = make_password(self.Pass_word)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """ Compare raw password with hashed password """
        return check_password(raw_password, self.Pass_word)
 

    def __str__(self):
        return self.T_name