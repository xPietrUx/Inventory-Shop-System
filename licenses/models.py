from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Software(models.Model):
    name = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.producer})"


class License(models.Model):
    software_id = models.ForeignKey(Software, on_delete=models.CASCADE)
    license_key = models.CharField(max_length=50, null=False)
    purchase_date = models.DateField()
    expiration_date = models.DateField(null=True)
    license_type = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
