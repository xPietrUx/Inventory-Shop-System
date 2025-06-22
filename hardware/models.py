from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class HardwareCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Hardware(models.Model):
    class HardwareStatus(models.TextChoices):
        IN_USE = "IU", "In use"
        IN_STORAGE = "IS", "In storage"
        IN_REPAIR = "IR", "In repair"
        UTILIZED = "UZ", "Utilized"

    inventory_number = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(HardwareCategory, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_to = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=HardwareStatus,
        default=HardwareStatus.IN_STORAGE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        old_status, old_user, old_project = None, None, None

        if not is_new:
            old_obj = Hardware.objects.get(pk=self.pk)
            old_status = old_obj.status
            old_user = old_obj.user
            old_project = old_obj.project

        # 1. if status is set to "In storage", "In repair" or "Utilized",
        #    hardware cannot be assigned to any project nor user
        if (
            self.status
            in [
                self.HardwareStatus.IN_STORAGE,
                self.HardwareStatus.IN_REPAIR,
                self.HardwareStatus.UTILIZED,
            ]
            and self.status != old_status
        ):
            self.user = None
            self.project = None
        # 2. if hardware is assigned to user or project its status HAS to be "In use"
        elif self.user or self.project:
            self.status = self.HardwareStatus.IN_USE
        # 3. if hardware is not assigned, and status is not "In repair" nor "Utilized",
        #    then its default status is "In storage"
        else:
            self.status = self.HardwareStatus.IN_STORAGE

        super().save(*args, **kwargs)

        if is_new:
            HardwareHistory.objects.create(
                hardware=self,
                event_date=timezone.now(),
                event_type=HardwareHistory.EventType.CREATED,
                description="Hardware created and added to storage.",
            )
        else:
            if (
                old_status != self.status
                or old_user != self.user
                or old_project != self.project
            ):
                event_type = None
                description = ""

                if self.status == self.HardwareStatus.IN_USE:
                    event_type = HardwareHistory.EventType.ASSIGNED
                    desc_parts = []
                    if self.user:
                        desc_parts.append(f"user: {self.user}")
                    if self.project:
                        desc_parts.append(f"project: {self.project}")
                    description = f"Assigned to {' and '.join(desc_parts)}."
                elif self.status == self.HardwareStatus.IN_STORAGE:
                    event_type = HardwareHistory.EventType.RETURNED
                    description = "Returned to storage."
                elif self.status == self.HardwareStatus.IN_REPAIR:
                    event_type = HardwareHistory.EventType.REPAIR
                    description = "Sent for repair."
                elif self.status == self.HardwareStatus.UTILIZED:
                    event_type = HardwareHistory.EventType.UTILIZED
                    description = "Hardware has been utilized."

                if event_type:
                    HardwareHistory.objects.create(
                        hardware=self,
                        event_date=timezone.now(),
                        event_type=event_type,
                        description=description,
                    )

    def __str__(self):
        return f"{self.name} ({self.inventory_number})"


class HardwareHistory(models.Model):
    class EventType(models.TextChoices):
        ASSIGNED = "ASSIGNED", "Assigned to user and/or project"
        RETURNED = "RETURNED", "Returned to storage"
        REPAIR = "REPAIR", "Sent for repair"
        UTILIZED = "UTILIZED", "Utilized"
        CREATED = "CREATED", "Created"

    hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_type = models.CharField(
        max_length=10, choices=EventType.choices, default=EventType.CREATED
    )
    description = models.TextField()
