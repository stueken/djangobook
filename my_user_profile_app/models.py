from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100, default="n.a.")
