from django import forms
from booking.forms import INDIAN_STATES, STATE_CITY_MAP


class CheckoutForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Make email read-only and populate from user
        if self.user:
            self.fields['email'].initial = self.user.email
            self.fields['email'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['class'] = 'form-control form-control-lg bg-light'
    name = forms.CharField(
        max_length=150,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Your full name',
            'autocomplete': 'off'
        })
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'you@example.com',
            'autocomplete': 'email'
        })
    )
    phone = forms.CharField(
        max_length=20,
        label='Phone Number',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': '+91 XXXXX XXXXX',
            'autocomplete': 'tel'
        })
    )
    address = forms.CharField(
        label='Street Address',
        widget=forms.Textarea(attrs={
            'rows': 2,
            'class': 'form-control form-control-lg',
            'placeholder': 'Street address'
        })
    )
    state = forms.ChoiceField(
        choices=INDIAN_STATES,
        label='State',
        widget=forms.Select(attrs={
            'class': 'form-control form-control-lg',
            'id': 'stateSelect'
        })
    )
    city = forms.CharField(
        max_length=120,
        label='City',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'id': 'citySelect',
            'placeholder': 'Select City'
        })
    )
    pincode = forms.CharField(
        max_length=15,
        label='PIN Code',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'PIN code',
            'pattern': '[0-9]{6}',
            'maxlength': '6'
        }),
        help_text='6-digit postal code'
    )





















