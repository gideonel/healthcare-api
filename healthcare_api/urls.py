from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Define the schema view for Swagger and ReDoc
schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare Appointment API",
        default_version='v1',
        description="API for managing healthcare appointments, including user registration, doctor management, and appointment scheduling.",
        terms_of_service="https://#/",
        contact=openapi.Contact(email="lordgideonel@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User-related endpoints
    path('users/', include('users.urls')),

    # Doctor-related endpoints
    path('doctors/', include('doctors.urls')),

    # Appointment-related endpoints
    path('appointments/', include('appointments.urls')),

    # DRF Authentication URLs
    path('api-auth/', include('rest_framework.urls')),

    # Swagger and ReDoc documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
