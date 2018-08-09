from django import forms
from django.utils.translation import gettext_lazy as _
from .models import *


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(label="",
                                   max_length=150,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': _('Email')}))

    class Meta:
        model = Subscriber
        fields = ('email',)
