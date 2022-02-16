from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    department = models.CharField(max_length=50, default=' ', null=True, blank=True)
    cell_phone = models.CharField(max_length=50, default=' ', null=True, blank=True)
    test = models.CharField(max_length=10)

