# apps/roles/models.py
from django.db import models
import uuid

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class RoleType(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        CUSTOMER = 'customer', 'Customer'
        OWNER = 'owner', 'Owner'

    name = models.CharField(
        max_length=50,
        choices=RoleType.choices,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'roles'