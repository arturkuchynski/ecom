from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('city', 'postal_code',)

    class Meta:
        model = Profile
