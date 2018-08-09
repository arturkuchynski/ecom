from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']
    # list_display =  [field.name for  field in Subscriber.meta.fields]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
