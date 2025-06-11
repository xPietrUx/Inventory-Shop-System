from django.db import models

# Create your models here.


class Users(models.Model):
    ID_User = models.BigAutoField(primary_key=True)
    Name = models.CharField()
    Surname = models.CharField()
    Email = models.EmailField(unique=True)
    Positon = models.CharField()
    ID_Role = models.ForeignKey("Role", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.Name} {self.Surname} na stanowisku: {self.Positon}"
