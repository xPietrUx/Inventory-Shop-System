from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Roles(models.Model):
    role_name = models.CharField()
    description = models.CharField()


class Users(AbstractUser):
    name = models.CharField()
    surname = models.CharField()
    email = models.EmailField(unique=True)
    position = models.CharField()
    id_role = models.ForeignKey("Role", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.Name} {self.Surname} na stanowisku: {self.position}"
