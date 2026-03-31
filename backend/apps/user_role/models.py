# apps/user_roles/models.py
from django.db import models
import uuid

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='user_role'
    )

    role = models.ForeignKey(
        'roles.Role',
        on_delete=models.CASCADE,
        related_name='user_role'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role')
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['role']),
        ]

    def __str__(self):
        return f"{self.user_id} - {self.role_id}"

    class Meta:
        db_table = 'user_role'