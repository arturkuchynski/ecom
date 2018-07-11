from django import forms
from .models import Order
from localflavor.ru.forms import RUPostalCodeField


class OrderCreateForm(forms.ModelForm):
    postal_code = RUPostalCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number',
                  'address', 'postal_code', 'city']
