from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserReadOnlyViewSet


router = DefaultRouter()
router.register(r'users', UserReadOnlyViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
