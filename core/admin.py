from django import forms
from django.contrib import admin

from core.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
