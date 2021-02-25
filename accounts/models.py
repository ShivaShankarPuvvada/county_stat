# account
from django.contrib import auth
from django.db import models
from django.utils import timezone
# from phone_field import PhoneField


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

# pip install django-phone-field
# https://pypi.org/project/django-phone-field/
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional items not defaulted in the Django User
    # phone = PhoneField(blank=True, help_text='Contact phone number')
    title = models.CharField(max_length=255)
    agency_name = models.ForeignKey('myapp.Agency', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
