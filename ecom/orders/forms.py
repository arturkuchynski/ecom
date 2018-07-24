from django import forms
from .models import Order
from localflavor.ru.forms import RUPostalCodeField
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class OrderCreateForm(forms.ModelForm):
    postal_code = RUPostalCodeField(label="",
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Postal Code')}))
    phone_number = PhoneNumberField(label="",
                                    widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Phone number')}))

    first_name = forms.CharField(label="",
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'First Name'}))

    last_name = forms.CharField(label="",
                                max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Last Name'}))


    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Email Address'}))

    city = forms.CharField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'City/Town'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'address', 'postal_code', 'city']
