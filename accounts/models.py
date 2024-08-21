from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    '''
        Extending the BaseUserManager, for the custom use
    '''
    def create_user(self, email, name, password=None, password2=None, address=None, phone_no=None):
        '''
            To create a simple user account
        '''
        
        if not email:
            raise ValueError('Email must be provided.')
        
        # create a user instance, using custom user model
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            address = address,
            phone_no = phone_no
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name,password=None):
        '''
            To create a superuser
        '''
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class Accounts(AbstractBaseUser):
    
    email = models.EmailField(verbose_name="email address",max_length=255,unique=True)
    name=models.CharField(verbose_name="Full Name", max_length=255)
    address = models.CharField(_("Address"), max_length=50, null=True)
    phone_no = models.IntegerField(_("Phone Number"), unique=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()


    def __str__(self):
        return self.email
    
    def has_perm(self, perm ,obj=None):
        "Does the user have a specific permission?"
        return self.is_admin
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'