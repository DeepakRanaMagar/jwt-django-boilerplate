from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

'''
    Extending the user model using AbstractBaseUser
'''
class Account(AbstractUser):
    name = models.CharField(_("full name"), max_length=50)
    email = models.EmailField(_("email"), max_length=254, unique=True)
    phone = models.IntegerField(_("phone_num"), unique=True)

    def __str__(self):
        return self.name
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']
    