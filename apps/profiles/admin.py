# apps/profiles/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.profiles.models import Profile, Skill

# Register your models here.

admin.site.register(Profile)
admin.site.register(Skill)