from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from localflavor.ru.forms import RUPostalCodeField
from phonenumber_field.formfields import PhoneNumberField
from users.models import Profile
from django import forms


class ChangeUserPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="",
                                   max_length=150,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': _('Old Password')}))

    new_password1 = forms.CharField(label="",
                                    max_length=150,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': _('New Password')}))

    new_password2 = forms.CharField(label="",
                                    max_length=150,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                      'placeholder': _('Confirm Password')}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditUserForm(UserChangeForm):
    first_name = forms.CharField(label="",
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'First Name'}))
    last_name = forms.CharField(label="",
                                max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Last Name'}))

    username = forms.CharField(label="",
                               max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username'}))

    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Email Address'}))

    # password = forms.CharField(label="",
    #                            widget=forms.PasswordInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class EditProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Profile.GENDER_CHOICES, widget=forms.RadioSelect)

    birth_date = forms.DateField(widget=forms.widgets.DateInput)

    phone_number = PhoneNumberField(label="", widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': _('Phone Number')}))
    postal_code = RUPostalCodeField(label="",
                                    widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Postal Code')}))
    address = forms.CharField(label="",
                              max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': _('Address')}))
    city = forms.CharField(label="",
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': _('City')}))

    class Meta:
        model = Profile
        fields = ('gender', 'birth_date', 'phone_number', 'postal_code', 'address', 'city')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': _('Email Address')}))
    first_name = forms.CharField(label="",
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': _('First Name')}))
    last_name = forms.CharField(label="",
                                max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': _('Last Name')}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = _("Username")
        self.fields['username'].label = ""

        self.fields['username'].help_text = _("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = _("Password")
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = _("Your password can\'t be too similar to your other personal "
                                               "information.\nYour "
                                               "password must contain at least 8 characters. Your password can\'t be "
                                               "a commonly" 
                                               "used password. Your password can\'t be entirely numeric. ")

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = _("Confirm Password")
        self.fields['password2'].help_text = _("Enter the same password as before, for verification.")
        self.fields['password2'].label = ""
