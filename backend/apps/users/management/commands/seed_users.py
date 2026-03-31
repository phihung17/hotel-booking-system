# apps/users/management/commands/seed_users.py

import json
from pathlib import Path
from django.core.management.base import BaseCommand
from apps.users.models import User
import os
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    help = "Seed users from JSON"

    def handle(self, *args, **kwargs):
        file_path = Path(__file__).resolve().parent.parent.parent / "seed-data" / "users.json"

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        for item in data:
            user, created = User.objects.get_or_create(
                id=item["id"],
                defaults={
                    "email": item["email"],
                    "first_name": item.get("first_name", ""),
                    "last_name": item.get("last_name", ""),
                    "phone": item.get("phone"),
                    "is_active": item.get("is_active", True),
                },
            )

            if created:
                password = item.get("password") or os.getenv("DEFAULT_PW")
                user.set_password(password)
                user.save()

                self.stdout.write(self.style.SUCCESS(f"Created: {user.email}"))
            else:
                self.stdout.write(self.style.WARNING(f"Exists: {user.email}"))

        self.stdout.write(self.style.SUCCESS("✅ Seed users done"))