# apps/users/management/commands/seed_users.py

import json
from pathlib import Path
from django.core.management.base import BaseCommand
from apps.user_role.models import UserRole


class Command(BaseCommand):
    help = "Seed user role from JSON"

    def handle(self, *args, **kwargs):
        file_path = Path(__file__).resolve().parent.parent.parent / "seed-data" / "user_role.json"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            user_role, created = UserRole.objects.get_or_create(
                id=item["id"],
                defaults={
                    "user_id": item["user_id"],
                    "role_id": item["role_id"],
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {user_role.user_id} - {user_role.role_id}"))
            else:
                self.stdout.write(self.style.WARNING(f"Exists: {user_role.user_id} - {user_role.role_id}"))

        self.stdout.write(self.style.SUCCESS("✅ Seed user role done"))