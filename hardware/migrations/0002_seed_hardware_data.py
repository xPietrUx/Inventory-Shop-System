from django.db import migrations
from django.utils import timezone


def create_data(apps, schema_editor):
    HardwareCategory = apps.get_model("hardware", "HardwareCategory")
    Project = apps.get_model("hardware", "Project")
    Hardware = apps.get_model("hardware", "Hardware")
    HardwareHistory = apps.get_model("hardware", "HardwareHistory")
    User = apps.get_model("users", "User")

    # Create Categories
    cat1 = HardwareCategory.objects.create(name="Laptop")
    cat2 = HardwareCategory.objects.create(name="Monitor")
    cat3 = HardwareCategory.objects.create(name="Keyboard")
    cat4 = HardwareCategory.objects.create(name="Docking Station")
    cat5 = HardwareCategory.objects.create(name="Printer")

    # Create Projects
    proj1 = Project.objects.create(name="Project Alpha", start_date=timezone.now())
    proj2 = Project.objects.create(name="Project Beta", start_date=timezone.now())
    proj3 = Project.objects.create(name="Project Gamma", start_date=timezone.now())

    # Create Users (assuming some users exist)
    # In a real scenario, you would fetch or create users.
    # For this seed, we'll fetch one of the users created in the users migration.
    try:
        user1 = User.objects.get(username="bwayne")
        user2 = User.objects.get(username="jdoe")
        user3 = User.objects.get(username="dprince")
        user4 = User.objects.get(username="ckent")
        user5 = User.objects.get(username="pparker")
        user6 = User.objects.get(username="lrose")
    except User.DoesNotExist:
        user1, user2, user3, user4, user5, user6 = None, None, None, None, None, None

    hardware_to_create = [
        {
            "inv_num": "NB-001",
            "name": "Dell XPS 15",
            "cat": cat1,
            "sn": "DXPS15-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 2),
            "status": "IU",
            "user": user1,
            "proj": proj1,
        },
        {
            "inv_num": "MON-001",
            "name": "Dell 27inch 4K",
            "cat": cat2,
            "sn": "D274K-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 3),
            "status": "IS",
            "user": None,
            "proj": None,
        },
        {
            "inv_num": "KEY-001",
            "name": "Logitech MX Keys",
            "cat": cat3,
            "sn": "LMXK-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365),
            "status": "IU",
            "user": user1,
            "proj": None,
        },
        {
            "inv_num": "NB-002",
            "name": "Apple Macbook Pro",
            "cat": cat1,
            "sn": "AMBP-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 2),
            "status": "IU",
            "user": user3,
            "proj": proj2,
        },
        {
            "inv_num": "MON-002",
            "name": "LG 34inch Ultrawide",
            "cat": cat2,
            "sn": "LG34UW-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 3),
            "status": "IR",
            "user": None,
            "proj": None,
        },
        {
            "inv_num": "KEY-002",
            "name": "Razer Blackwidow",
            "cat": cat3,
            "sn": "RBW-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365),
            "status": "UZ",
            "user": None,
            "proj": None,
        },
        {
            "inv_num": "NB-003",
            "name": "Lenovo Thinkpad",
            "cat": cat1,
            "sn": "LTP-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 2),
            "status": "IU",
            "user": user4,
            "proj": proj1,
        },
        {
            "inv_num": "DS-001",
            "name": "CalDigit TS4",
            "cat": cat4,
            "sn": "CDTS4-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365),
            "status": "IU",
            "user": user6,
            "proj": proj3,
        },
        {
            "inv_num": "PRN-001",
            "name": "HP LaserJet Pro",
            "cat": cat5,
            "sn": "HPLJP-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 2),
            "status": "IS",
            "user": None,
            "proj": None,
        },
        {
            "inv_num": "NB-004",
            "name": "Microsoft Surface Laptop",
            "cat": cat1,
            "sn": "MSL-001",
            "purchase": timezone.now(),
            "warranty": timezone.now() + timezone.timedelta(days=365 * 2),
            "status": "IU",
            "user": user5,
            "proj": proj2,
        },
    ]

    for hw_data in hardware_to_create:
        hardware_item, created = Hardware.objects.get_or_create(
            inventory_number=hw_data["inv_num"],
            defaults={
                "name": hw_data["name"],
                "category": hw_data["cat"],
                "serial_number": hw_data["sn"],
                "purchase_date": hw_data["purchase"],
                "warranty_to": hw_data["warranty"],
                "status": hw_data["status"],
                "user": hw_data["user"],
                "project": hw_data["proj"],
            },
        )

        if created:
            HardwareHistory.objects.create(
                hardware=hardware_item,
                event_date=hardware_item.purchase_date,
                event_type="CREATED",
                description="Hardware created and added to storage via migration.",
            )
            if hardware_item.status == "IU":
                desc = "Assigned via migration"
                if hardware_item.user:
                    desc += f" to user: {hardware_item.user}"
                if hardware_item.project:
                    desc += f" for project: {hardware_item.project}"
                HardwareHistory.objects.create(
                    hardware=hardware_item,
                    event_date=hardware_item.purchase_date,
                    event_type="ASSIGNED",
                    description=desc,
                )


def remove_data(apps, schema_editor):
    HardwareCategory = apps.get_model("hardware", "HardwareCategory")
    Project = apps.get_model("hardware", "Project")
    Hardware = apps.get_model("hardware", "Hardware")
    HardwareCategory.objects.all().delete()
    Project.objects.all().delete()
    Hardware.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0001_initial"),
        ("users", "0003_seed_users"),
    ]

    operations = [
        migrations.RunPython(create_data, remove_data),
    ]
