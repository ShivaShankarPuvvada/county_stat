# myapp
from django.db import models
from django.contrib.auth.models import User 


class Agency(models.Model):
    system_name = models.CharField(max_length=255)
    county = models.CharField(max_length=60)
    state = models.CharField(max_length=2)
    active = models.BooleanField(default=True)

    system_type_tuple = [('C', 'Community'),('NC','Non-Community'),('NP','No Political boundary'),('TC','Temporary Community'),('UN','Unknown')]
    system_type = models.CharField(max_length=2, choices=system_type_tuple, default= 'UN')
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=60, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    def __str__(self):
        return self.system_name

class SystemNumber(models.Model):
    sys_name = models.ForeignKey(Agency, on_delete=models.CASCADE)
    system_no = models.CharField(max_length=7, unique=True)
    def __str__(self):
        return self.system_no

class County(models.Model):
    pass
