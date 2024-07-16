from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

'''
    Extending the user model using AbstractBaseUser
'''

class CustomUserManager(BaseUserManager):
    '''
        Handles schema for the Custom user manager, which extends from BaseUserManager
    '''
    def create_user(self, phone_no, password=None):
        if not phone_no:
            raise ValueError('Users must have a phone number')
        user = self.model(phone_no=phone_no)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_no, password):
        user = self.create_user(phone_no, password)
        user.is_admin = True
        user.save()
        return user

class Account(AbstractBaseUser):
    '''
        Handles the schema for the Account model
    '''
    phone_no = models.IntegerField(_("Phone Number"), unique=True)
    name = models.CharField(_("Name"), max_length=50)
    joined_date = models.DateTimeField(_("joined data"), auto_now_add=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    
    # calling the CustomUserManager()
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_no'

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin