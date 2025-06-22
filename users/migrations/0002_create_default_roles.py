from django.db import migrations


def create_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.get_or_create(name="Admin")
    Role.objects.get_or_create(name="Operator")


def remove_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.filter(name__in=["Admin", "Operator"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_roles, remove_roles),
    ]
