from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # filterset_fields = ['is_active']

    search_fields = ['email', 'first_name', 'last_name', 'phone']

    ordering_fields = ['created_at', 'email']
    ordering = ['-created_at']

    # Only get users with role customer or owner
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(roles__name__in=['customer', 'owner'])
            .prefetch_related('roles')
            .distinct()
        )