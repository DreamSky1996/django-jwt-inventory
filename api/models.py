from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    class ROLES(models.IntegerChoices):
        READ = 0
        MANAGE = 1
        READ_AND_MANAGE = 2
        ADMIN = 3
    role = models.IntegerField(choices=ROLES.choices, default=0)
    