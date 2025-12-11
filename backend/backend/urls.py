from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.schemas import get_schema_view
from django.http import JsonResponse
from django.urls import re_path


def root_view(request):
    return JsonResponse({"message": "Backend is running"})


schema_view = get_schema_view(title="Django API")



urlpatterns = [
    re_path(r'^$', root_view),  # Root path, works even with Choreo prefixes
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
    path("openapi/", schema_view, name="openapi-schema"),
]


