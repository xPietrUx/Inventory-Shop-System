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


def remove_users(apps, schema_editor):
    User = apps.get_model("users", "User")
    User.objects.filter(username__in=["bwayne", "jdoe"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_create_default_roles"),
    ]

    operations = [
        migrations.RunPython(create_users, remove_users),
    ]
