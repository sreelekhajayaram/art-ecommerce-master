from django import forms
from .models import PortraitBooking


INDIAN_STATES = [
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra and Nagar Haveli and Daman and Diu','Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
]


SIZE_CHOICES = [
    ('A3', 'A3 (297 x 420 mm)'),
    ('A4', 'A4 (210 x 297 mm)'),
    ('A5', 'A5 (148 x 210 mm)'),
]


class PortraitBookingForm(forms.ModelForm):
    class Meta:
        model = PortraitBooking
        # state placed before city per request; category added
        fields = [
            'name', 'email', 'phone', 'preferred_date',
            'address', 'state', 'city', 'pincode',
            'category', 'size', 'reference_image', 'description', 'price'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+91...'}),
            'preferred_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.Select(choices=INDIAN_STATES, attrs={'class': 'form-control', 'id': 'stateSelect'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PIN code'}),
            'reference_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'size': forms.Select(choices=SIZE_CHOICES, attrs={'class': 'form-control', 'id': 'sizeSelect'}),
            'category': forms.Select(choices=PortraitBooking.CATEGORY_CHOICES, attrs={'class': 'form-control', 'id': 'categorySelect'}),
            'price': forms.HiddenInput(attrs={'id': 'priceInput'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure visible ordering and add bootstrap classes if any field missing attrs
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control'



















