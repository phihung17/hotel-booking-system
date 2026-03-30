# apps/users/management/commands/seed_users.py

import json
from pathlib import Path
from django.core.management.base import BaseCommand
from apps.roles.models import Role


class Command(BaseCommand):
    help = "Seed roles from JSON"

    def handle(self, *args, **kwargs):
        file_path = Path(__file__).resolve().parent.parent.parent / "seed-data" / "roles.json"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            role, created = Role.objects.get_or_create(
                id=item["id"],
                defaults={
                    "name": item["name"],
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {role.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Exists: {role.name}"))

        self.stdout.write(self.style.SUCCESS("✅ Seed roles done"))