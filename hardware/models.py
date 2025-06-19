from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class HardwareCategory(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    supervisor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class Hardware(models.Model):
    class HardwareStatus(models.TextChoices):
        IN_USE = "IU", "In use"
        IN_STORAGE = "IS", "In storage"
        IN_REPAIR = "IR", "In repair"
        UTILIZED = "UZ", "Utilized"

    inventory_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(HardwareCategory, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_to = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=HardwareStatus,
        default=HardwareStatus.IN_STORAGE,
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)


class HardwareHistory(models.Model):
    class EventType(models.TextChoices):
        ASSIGNED = "ASSIGNED", "Assigned to user"
        RETURNED = "RETURNED", "Returned to storage"
        REPAIR = "REPAIR", "Sent for repair"
        UTILIZED = "UTILIZED", "Utilized"
        CREATED = "CREATED", "Created"

    hardware_id = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_type = models.CharField(
        max_length=10, choices=EventType.choices, default=EventType.CREATED
    )
    description = models.TextField()
