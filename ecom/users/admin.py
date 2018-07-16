from django.contrib import admin
from .models import *

@admin.register(Profile)
class BookImageAdmin(admin.ModelAdmin):
    # list_display = ('book', 'created', 'updated',)
    # list_filter = ('book',)

    class Meta:
        model = Profile
# Register your models here.
