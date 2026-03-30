from rest_framework import serializers
from .models import User

# Like DTO
class UserSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'created_at',
            'roles'
        ]

    def get_roles(self, obj):
        return [
            {
                "name": ur.role.name,
                "assigned_at": ur.created_at
            }
            for ur in obj.user_role.all()
        ]