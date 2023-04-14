from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from {{cookiecutter.project_slug}}.authn.views import UserViewSet


users_router = routers.DefaultRouter()
users_router.register(r'users', UserViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),

    # API
    path("api/", include((users_router.urls, "users")))
]