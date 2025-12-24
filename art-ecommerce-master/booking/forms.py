from django import forms
from .models import PortraitBooking
import json


INDIAN_STATES = [
    ('', 'Select State'),
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

# State-City Mapping for dynamic dropdown
STATE_CITY_MAP = {
    'Andhra Pradesh': ['Hyderabad', 'Vijayawada', 'Visakhapatnam', 'Tirupati', 'Kakinada'],
    'Arunachal Pradesh': ['Itanagar', 'Naharlagun', 'Changlang'],
    'Assam': ['Guwahati', 'Dibrugarh', 'Silchar', 'Nagaon', 'Tinsukia'],
    'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Darbhanga', 'Arrah'],
    'Chandigarh': ['Chandigarh'],
    'Chhattisgarh': ['Raipur', 'Bhilai', 'Durg', 'Bilaspur', 'Rajnandgaon'],
    'Delhi': ['New Delhi', 'Delhi'],
    'Goa': ['Panaji', 'Margao', 'Vasco da Gama', 'Ponda'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Jamnagar', 'Gandhinagar', 'Bhavnagar'],
    'Haryana': ['Faridabad', 'Gurgaon', 'Hisar', 'Rohtak', 'Panipat', 'Yamunanagar'],
    'Himachal Pradesh': ['Shimla', 'Solan', 'Mandi', 'Kangra', 'Kullu', 'Hamirpur'],
    'Jharkhand': ['Ranchi', 'Dhanbad', 'Jamshedpur', 'Giridih', 'Bokaro'],
    'Karnataka': ['Bangalore', 'Mangalore', 'Mysore', 'Belgaum', 'Hubli', 'Davangere', 'Kochi'],
    'Kerala': ['Kochi', 'Thiruvananthapuram', 'Kozhikode', 'Kottayam', 'Kannur', 'Palakkad'],
    'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Ujjain', 'Gwalior', 'Sagar'],
    'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Aurangabad', 'Nashik', 'Kolhapur'],
    'Manipur': ['Imphal', 'Bishnupur'],
    'Meghalaya': ['Shillong', 'Tura'],
    'Mizoram': ['Aizawl', 'Lunglei'],
    'Nagaland': ['Kohima', 'Dimapur'],
    'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Sambalpur', 'Berhampur'],
    'Puducherry': ['Puducherry', 'Yanam', 'Karaikal'],
    'Punjab': ['Ludhiana', 'Amritsar', 'Chandigarh', 'Jalandhar', 'Patiala', 'Bathinda'],
    'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota', 'Ajmer', 'Bhilwara', 'Bikaner'],
    'Sikkim': ['Gangtok', 'Pelling'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Salem', 'Tiruchirappalli', 'Tiruppur'],
    'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad'],
    'Tripura': ['Agartala', 'Udaipur'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Agra', 'Varanasi', 'Meerut', 'Noida', 'Ghaziabad'],
    'Uttarakhand': ['Dehradun', 'Haridwar', 'Almora', 'Nainital', 'Rishikesh'],
    'West Bengal': ['Kolkata', 'Asansol', 'Siliguri', 'Darjeeling', 'Howrah'],
    'Andaman and Nicobar Islands': ['Port Blair', 'Car Nicobar'],
    'Dadra and Nagar Haveli and Daman and Diu': ['Silvassa', 'Daman', 'Diu'],
    'Jammu and Kashmir': ['Srinagar', 'Jammu', 'Leh'],
    'Ladakh': ['Leh', 'Kargil'],
    'Lakshadweep': ['Kavaratti', 'Agatti'],
}

SIZE_CHOICES_WITH_DESC = [
    ('8x10', '8" × 10"'),
    ('A4', '8.3" × 11.7" (A4)'),
    ('11x14', '11" × 14"'),
    ('A3', '11.7" × 16.5" (A3)'),
    ('16x20', '16" × 20"'),
    ('A2', '16.5" × 23.4" (A2)'),
]

SIZE_DESCRIPTIONS = {
    '8x10': {
        'title': '8" × 10"',
        'description': 'Small, detailed portrait or single subject artwork. Best for close-up facial studies.',
        'ideal': '✓ Best for: Single portrait, face close-up | Perfect for: Desk, shelf, small wall'
    },
    'A4': {
        'title': '8.3" × 11.7" (A4)',
        'description': 'Single head-and-shoulders portrait with balanced composition. Ideal for quick commissions.',
        'ideal': '✓ Best for: Portrait paintings, pencil drawings | Perfect for: Compact spaces, desks'
    },
    '11x14': {
        'title': '11" × 14"',
        'description': 'Single or couple portraits with shoulder-to-torso view. Great detail and presence.',
        'ideal': '✓ Best for: Paintings, stencil art, couple portraits | Perfect for: Bedroom, living room'
    },
    'A3': {
        'title': '11.7" × 16.5" (A3)',
        'description': 'Couple or two-figure portraits with rich detail. Excellent for detailed stencil artwork.',
        'ideal': '✓ Best for: Detailed paintings, stencil art, couple compositions | Perfect for: Gallery walls'
    },
    '16x20': {
        'title': '16" × 20"',
        'description': 'Statement artwork or family portraits (up to 3 people). Maximum detail and impact.',
        'ideal': '✓ Best for: Family portraits, large paintings, caricatures | Perfect for: Living room focal point'
    },
    'A2': {
        'title': '16.5" × 23.4" (A2)',
        'description': 'Large premium artwork with exceptional visual presence. Perfect for showcase pieces.',
        'ideal': '✓ Best for: Premium paintings, group portraits, exhibition art | Perfect for: Statement wall'
    },
}


class PortraitBookingForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter your username',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = PortraitBooking
        # Removed 'preferred_date' field as per requirement
        fields = [
            'name', 'email', 'phone',
            'address', 'state', 'city', 'pincode',
            'category', 'size', 'reference_image', 'description', 'price'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Your full name',
                'autocomplete': 'off'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'you@example.com',
                'autocomplete': 'email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '+91 XXXXX XXXXX',
                'autocomplete': 'tel'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control form-control-lg',
                'placeholder': 'Describe your vision for the artwork...'
            }),
            'address': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control form-control-lg',
                'placeholder': 'Street address'
            }),
            'city': forms.Select(attrs={
                'class': 'form-control form-control-lg',
                'id': 'citySelect'
            }),
            'state': forms.Select(
                choices=INDIAN_STATES,
                attrs={
                    'class': 'form-control form-control-lg',
                    'id': 'stateSelect'
                }
            ),
            'pincode': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'PIN code',
                'pattern': '[0-9]{6}',
                'maxlength': '6'
            }),
            'reference_image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            }),
            'size': forms.Select(
                choices=SIZE_CHOICES_WITH_DESC,
                attrs={
                    'class': 'form-control form-control-lg',
                    'id': 'sizeSelect'
                }
            ),
            'category': forms.Select(
                choices=PortraitBooking.CATEGORY_CHOICES,
                attrs={
                    'class': 'form-control form-control-lg',
                    'id': 'categorySelect'
                }
            ),
            'price': forms.HiddenInput(attrs={'id': 'priceInput'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Update city field to be a select with dynamic options
        self.fields['city'] = forms.ChoiceField(
            choices=[('', 'Select City')],
            widget=forms.Select(attrs={
                'class': 'form-control form-control-lg',
                'id': 'citySelect'
            })
        )
        # Add labels with proper formatting
        self.fields['name'].label = 'Full Name'
        self.fields['email'].label = 'Email Address'
        self.fields['phone'].label = 'Phone Number'
        self.fields['address'].label = 'Street Address'
        self.fields['state'].label = 'State'
        self.fields['city'].label = 'City'
        self.fields['pincode'].label = 'PIN Code'
        self.fields['reference_image'].label = 'Upload Reference Image'
        self.fields['size'].label = 'Artwork Size'
        self.fields['category'].label = 'Artwork Category'
        self.fields['description'].label = 'Additional Details'
        
        # Add help text
        self.fields['pincode'].help_text = '6-digit postal code'
        self.fields['reference_image'].help_text = 'Upload a clear reference image (JPG, PNG)'



















