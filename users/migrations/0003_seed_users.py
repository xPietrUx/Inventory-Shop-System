from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_users(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    User = apps.get_model("users", "User")

    try:
        admin_role = Role.objects.get(name="Admin")
        operator_role = Role.objects.get(name="Operator")
    except Role.DoesNotExist:
        # This will fail if the roles are not created, the dependency should prevent this
        return

    User.objects.get_or_create(
        username="bwayne",
        defaults={
            "first_name": "Bruce",
            "last_name": "Wayne",
            "email": "bruce@wayne.com",
            "password": make_password("gotham"),
            "role": admin_role,
        },
    )

    User.objects.get_or_create(
        username="jdoe",
        defaults={
            "first_name": "Joe",
            "last_name": "Doe",
            "email": "joe.doe@example.com",
            "password": make_password("password123"),
            "role": operator_role,
        },
    )

    User.objects.get_or_create(
        username="dprince",
        defaults={
            "first_name": "Diana",
            "last_name": "Prince",
            "email": "diana@themyscira.com",
            "password": make_password("wonder"),
            "role": admin_role,
        },
    )

    User.objects.get_or_create(
        username="ckent",
        defaults={
            "first_name": "Clark",
            "last_name": "Kent",
            "email": "clark@dailyplanet.com",
            "password": make_password("superman"),
            "role": operator_role,
        },
    )

    User.objects.get_or_create(
        username="pparker",
        defaults={
            "first_name": "Peter",
            "last_name": "Parker",
            "email": "peter@dailybugle.com",
            "password": make_password("spidey"),
            "role": operator_role,
        },
    )

    User.objects.get_or_create(
        username="tstark",
        defaults={
            "first_name": "Tony",
            "last_name": "Stark",
            "email": "tony@stark.com",
            "password": make_password("ironman"),
            "role": admin_role,
        },
    )

    User.objects.get_or_create(
        username="nromanoff",
        defaults={
            "first_name": "Natasha",
            "last_name": "Romanoff",
            "email": "natasha@shield.com",
            "password": make_password("blackwidow"),
            "role": operator_role,
        },
    )


def remove_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.filter(
        username__in=[
            "bwayne",
            "jdoe",
            "dprince",
            "ckent",
            "pparker",
            "tstark",
            "nromanoff",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_create_default_roles"),
    ]

    operations = [
        migrations.RunPython(create_users, remove_users),
    ]
