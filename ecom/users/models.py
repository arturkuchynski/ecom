from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
        (2, 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.SmallIntegerField(
        choices=GENDER_CHOICES,
        default=0,
        blank=True,
        null=True,
    )

    birth_date = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(_('phone number'), blank=True)
    postal_code = models.CharField(_('postal code'),null=True, blank=True, max_length=20)
    address = models.CharField(_('address'),null=True, blank=True, max_length=250)
    city = models.CharField(_('city'), null=True, blank=True, max_length=100)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
