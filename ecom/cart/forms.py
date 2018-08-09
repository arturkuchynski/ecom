from django import forms
from django.utils.translation import gettext_lazy as _


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=[(ch, str(ch)) for ch in range(1, 5)],
                                      coerce=int,
                                      label=_('Quantity'),
                                      )

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput,
                                label=_('Update'))

    def __init__(self, *args, **kwargs):
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        # set custom styles
        self.fields['quantity'].widget.attrs['class'] = 'selectpicker'
