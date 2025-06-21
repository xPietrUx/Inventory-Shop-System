from django.db import migrations
from datetime import date


def seed_data(apps, schema_editor):
    User = apps.get_model("users", "Users")
    HardwareCategory = apps.get_model("hardware", "HardwareCategory")
    Project = apps.get_model("hardware", "Project")
    Hardware = apps.get_model("hardware", "Hardware")
    HardwareHistory = apps.get_model("hardware", "HardwareHistory")

    # --- Get Users (assuming they were created by the licenses seed) ---
    try:
        user_jdoe = User.objects.get(username="jdoe_seed")
        user_asmith = User.objects.get(username="asmith_seed")
        user_bwayne = User.objects.get(username="bwayne_seed")
    except User.DoesNotExist:
        print(
            "!!! BŁĄD: Użytkownicy testowi nie istnieją. Uruchom najpierw migrację 'licenses'."
        )
        return

    # --- Create Hardware Categories ---
    cat_laptop, _ = HardwareCategory.objects.get_or_create(name="Laptop")
    cat_monitor, _ = HardwareCategory.objects.get_or_create(name="Monitor")
    cat_keyboard, _ = HardwareCategory.objects.get_or_create(name="Keyboard")
    cat_mouse, _ = HardwareCategory.objects.get_or_create(name="Mouse")

    # --- Create Projects ---
    proj_alpha, _ = Project.objects.get_or_create(
        name="Project Alpha",
        defaults={
            "description": "Development of a new web platform.",
            "supervisor_id": user_bwayne,
            "start_date": date(2023, 1, 1),
            "end_date": date(2024, 12, 31),
        },
    )
    proj_beta, _ = Project.objects.get_or_create(
        name="Project Beta",
        defaults={
            "description": "Internal infrastructure upgrade.",
            "supervisor_id": user_bwayne,
            "start_date": date(2023, 6, 1),
        },
    )

    # --- Create Hardware and History ---
    hardware_to_create = [
        {
            "inv_num": "LAP-001",
            "name": "Dell XPS 15",
            "cat": cat_laptop,
            "sn": "DXPS15-SN001",
            "purchase": date(2023, 2, 10),
            "warranty": date(2026, 2, 9),
            "status": "IU",
            "user": user_jdoe,
            "proj": proj_alpha,
        },
        {
            "inv_num": "MON-001",
            "name": "Dell U2721DE",
            "cat": cat_monitor,
            "sn": "DU27-SN001",
            "purchase": date(2023, 2, 10),
            "warranty": date(2026, 2, 9),
            "status": "IU",
            "user": user_jdoe,
            "proj": None,
        },
        {
            "inv_num": "LAP-002",
            "name": "MacBook Pro 14",
            "cat": cat_laptop,
            "sn": "MBP14-SN002",
            "purchase": date(2023, 5, 20),
            "warranty": date(2026, 5, 19),
            "status": "IU",
            "user": user_asmith,
            "proj": proj_alpha,
        },
        {
            "inv_num": "LAP-003",
            "name": "Lenovo ThinkPad X1",
            "cat": cat_laptop,
            "sn": "LTPX1-SN003",
            "purchase": date(2022, 11, 15),
            "warranty": date(2025, 11, 14),
            "status": "IS",
            "user": None,
            "proj": None,
        },
        {
            "inv_num": "KEY-001",
            "name": "Logitech MX Keys",
            "cat": cat_keyboard,
            "sn": "LMXK-SN001",
            "purchase": date(2023, 2, 10),
            "warranty": date(2025, 2, 9),
            "status": "IU",
            "user": user_jdoe,
            "proj": None,
        },
    ]

    for hw_data in hardware_to_create:
        hardware_item, created = Hardware.objects.get_or_create(
            inventory_number=hw_data["inv_num"],
            defaults={
                "name": hw_data["name"],
                "category_id": hw_data["cat"],
                "serial_number": hw_data["sn"],
                "purchase_date": hw_data["purchase"],
                "warranty_to": hw_data["warranty"],
                "status": hw_data["status"],
                "user_id": hw_data["user"],
                "project_id": hw_data["proj"],
            },
        )
        if created:
            HardwareHistory.objects.create(
                hardware_id=hardware_item,
                event_date=hardware_item.purchase_date,
                event_type="CREATED",
                description="Hardware added to inventory.",
            )
            if hardware_item.user_id:
                HardwareHistory.objects.create(
                    hardware_id=hardware_item,
                    event_date=hardware_item.purchase_date,
                    event_type="ASSIGNED",
                    description=f"Assigned to user {hardware_item.user_id.username}.",
                )


def remove_data(apps, schema_editor):
    HardwareCategory = apps.get_model("hardware", "HardwareCategory")
    Project = apps.get_model("hardware", "Project")
    Hardware = apps.get_model("hardware", "Hardware")
    HardwareHistory = apps.get_model("hardware", "HardwareHistory")

    # Delete in reverse order of creation to respect dependencies
    HardwareHistory.objects.filter(
        hardware_id__inventory_number__in=[
            "LAP-001",
            "MON-001",
            "LAP-002",
            "LAP-003",
            "KEY-001",
        ]
    ).delete()
    Hardware.objects.filter(
        inventory_number__in=["LAP-001", "MON-001", "LAP-002", "LAP-003", "KEY-001"]
    ).delete()
    Project.objects.filter(name__in=["Project Alpha", "Project Beta"]).delete()
    HardwareCategory.objects.filter(
        name__in=["Laptop", "Monitor", "Keyboard", "Mouse", "Docking Station"]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0001_initial"),
        (
            "licenses",
            "0003_seed_software_licenses",
        ),  # Depends on users from licenses seed
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
