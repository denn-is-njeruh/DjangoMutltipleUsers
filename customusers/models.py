from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active =  models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "i/users/%i/" % (self.pk)

    def get_email(self):
        return self.email


# class user_type(models.Model):
#     is_teach = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_student == True:
#             return User.get_email(self.user) + " - is_student"
#         else:
#             return User.get_email(self.user) + "- is_teacher"
    
