from django.db import migrations
from django.utils import timezone


def create_license_data(apps, schema_editor):
    Software = apps.get_model("licenses", "Software")
    License = apps.get_model("licenses", "License")
    User = apps.get_model("users", "User")

    # Get users created in the previous migration
    try:
        bwayne = User.objects.get(username="bwayne")
    except User.DoesNotExist:
        bwayne = None

    # Create Software
    software1 = Software.objects.create(
        name="Microsoft Office 365", producer="Microsoft"
    )
    software2 = Software.objects.create(name="Adobe Photoshop", producer="Adobe")

    # Create Licenses
    License.objects.create(
        software=software1,
        license_key="OFFICE-365-KEY-123",
        purchase_date=timezone.now(),
        expiration_date=timezone.now() + timezone.timedelta(days=365),
        user=bwayne,
    )

    License.objects.create(
        software=software2,
        license_key="PHOTOSHOP-KEY-456",
        purchase_date=timezone.now(),
        expiration_date=None,  # Perpetual license
        user=bwayne,
    )


def remove_license_data(apps, schema_editor):
    Software = apps.get_model("licenses", "Software")
    License = apps.get_model("licenses", "License")
    Software.objects.all().delete()
    License.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("licenses", "0001_initial"),
        ("users", "0003_seed_users"),
    ]

    operations = [
        migrations.RunPython(create_license_data, remove_license_data),
    ]
