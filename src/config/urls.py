from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import include, path


schema_view = get_schema_view(
   openapi.Info(
      title="Docs REST API",
      default_version='v1',
      description="Coins Transfer API",
      contact=openapi.Contact(email="pawelpilichowski@sygnal24.pl"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('api/v1/', include('apps.user.urls')),
    path('admin/', admin.site.urls),
    path("auth/", include("rest_framework.urls")),
]
