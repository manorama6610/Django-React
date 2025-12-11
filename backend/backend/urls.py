from django.contrib import admin
from django.urls import path, include, re_path
from api.views import CreateUserView, health_check
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "Backend is running"})

schema_view = get_schema_view(title="Django API")

urlpatterns = [
    re_path(r'^.*$', root_view),  # catch-all root for Choreo
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    path("api/health/", health_check),  # dedicated health endpoint
    path("openapi/", schema_view, name="openapi-schema"),
]
