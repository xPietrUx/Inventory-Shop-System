from django.db import migrations

def seed_roles(apps, schema_editor):
    Roles = apps.get_model('users', 'Roles')
    Roles.objects.create(role_name='Admin', description='Administrator role with full permissions.')
    Roles.objects.create(role_name='Operator', description='Operator role with limited permissions.')

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_roles),
    ]
