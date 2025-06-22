from django.db import migrations
from django.utils import timezone


def create_license_data(apps, schema_editor):
    Software = apps.get_model("licenses", "Software")
    License = apps.get_model("licenses", "License")
    User = apps.get_model("users", "User")

    # Get users created in the previous migration
    try:
        bwayne = User.objects.get(username="bwayne")
        dprince = User.objects.get(username="dprince")
        ckent = User.objects.get(username="ckent")
        tstark = User.objects.get(username="tstark")
        nromanoff = User.objects.get(username="nromanoff")
        jdoe = User.objects.get(username="jdoe")
    except User.DoesNotExist:
        bwayne, dprince, ckent, tstark, nromanoff, jdoe = (None,) * 6

    # Create Software
    software1 = Software.objects.create(
        name="Microsoft Office 365", producer="Microsoft"
    )
    software2 = Software.objects.create(name="Adobe Photoshop", producer="Adobe")
    software3 = Software.objects.create(
        name="Jetbrains PyCharm", producer="Jetbrains"
    )
    software4 = Software.objects.create(name="Autodesk AutoCAD", producer="Autodesk")
    software5 = Software.objects.create(name="Final Cut Pro", producer="Apple")
    software6 = Software.objects.create(name="Sketch", producer="Sketch")

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
        user=dprince,
    )

    License.objects.create(
        software=software3,
        license_key="PYCHARM-KEY-789",
        purchase_date=timezone.now(),
        expiration_date=timezone.now() + timezone.timedelta(days=365),
        user=ckent,
    )

    License.objects.create(
        software=software4,
        license_key="AUTOCAD-KEY-101",
        purchase_date=timezone.now(),
        expiration_date=None,  # Perpetual license
        user=jdoe,
    )

    License.objects.create(
        software=software5,
        license_key="FCP-KEY-111",
        purchase_date=timezone.now(),
        expiration_date=None,  # Perpetual license
        user=tstark,
    )

    License.objects.create(
        software=software6,
        license_key="SKETCH-KEY-222",
        purchase_date=timezone.now(),
        expiration_date=timezone.now() + timezone.timedelta(days=365),
        user=nromanoff,
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
