from django.db import migrations


def create_roles(apps, schema_editor):
    Role = apps.get_model("users", "Role")
    Role.objects.create(
        name="Admin", description="Administrator role with full permissions."
    )
    Role.objects.create(
        name="Operator", description="Operator role with limited permissions."
    )


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
