from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from {{cookiecutter.project_slug}}.authn.models import User


admin.site.register(User, UserAdmin)