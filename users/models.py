from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField()
    surname = models.CharField()
    email = models.EmailField(unique=True)
    positon = models.CharField()
    id_role = models.ForeignKey("Role", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.Name} {self.Surname} na stanowisku: {self.Positon}"
