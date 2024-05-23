
from django.contrib.auth.models import AbstractUser,Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    app1_access = models.BooleanField(default=False)
    app2_access = models.BooleanField(default=False)
    app3_access = models.BooleanField(default=False)
    app4_access = models.BooleanField(default=False)
    app5_access = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

# Create your models here.
