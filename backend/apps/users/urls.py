from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import LoginView, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
] + router.urls