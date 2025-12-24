# 📝 Booking Form - Code Reference

## Complete Implementation Reference

---

## 1️⃣ STATE-CITY MAPPING DATA

This is the complete state-city mapping included in `booking/forms.py`:

```python
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
```

---

## 2️⃣ SIZE DESCRIPTIONS DATA

All size descriptions used in tooltips:

```python
SIZE_DESCRIPTIONS = {
    '8x10': {
        'title': '8" × 10"',
        'description': 'Small, detailed artwork with a single close-up subject.',
        'ideal': 'Ideal for desks, shelves, or as part of a gallery wall.'
    },
    'A4': {
        'title': '8.3" × 11.7" (A4)',
        'description': 'Single head-and-shoulders portrait.',
        'ideal': 'Perfect for desks, compact wall spaces, and easy framing.'
    },
    '11x14': {
        'title': '11" × 14"',
        'description': 'Single or couple portraits with more detail than 8×10.',
        'ideal': 'Versatile size suitable for various rooms and professional portraits.'
    },
    'A3': {
        'title': '11.7" × 16.5" (A3)',
        'description': 'Couple or two-figure portraits (up to shoulders), or detailed single subjects.',
        'ideal': 'Creates a strong visual impact and fits most room walls.'
    },
    '16x20': {
        'title': '16" × 20"',
        'description': 'Statement artwork or family portraits (up to 3 people) with rich detail.',
        'ideal': 'Best as a focal point above a couch, mantel, or large wall.'
    },
    'A2': {
        'title': '16.5" × 23.4" (A2)',
        'description': 'Large, premium artwork with high visual presence.',
        'ideal': 'Ideal for spacious interiors and prominent display areas.'
    },
}
```

---

## 3️⃣ JAVASCRIPT - STATE-CITY DEPENDENCY

Complete JavaScript code for state-city dynamic population:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // State-City Mapping Data
    const stateCityMap = {{ state_city_map|safe }};
    const sizeDescriptions = {{ size_descriptions|safe }};

    const stateSelect = document.getElementById('stateSelect');
    const citySelect = document.getElementById('citySelect');
    const sizeSelect = document.getElementById('sizeSelect');
    const sizeInfo = document.getElementById('sizeInfo');

    // Handle State Change
    if (stateSelect) {
        stateSelect.addEventListener('change', function() {
            const selectedState = this.value;
            citySelect.innerHTML = '<option value="">Select City</option>';

            if (selectedState && stateCityMap[selectedState]) {
                const cities = stateCityMap[selectedState];
                cities.forEach(city => {
                    const option = document.createElement('option');
                    option.value = city;
                    option.textContent = city;
                    citySelect.appendChild(option);
                });
                citySelect.disabled = false;
            } else {
                citySelect.disabled = true;
            }
        });
    }

    // Handle Size Selection - Show Hint Box
    if (sizeSelect) {
        sizeSelect.addEventListener('change', function() {
            const selectedSize = this.value;
            
            if (selectedSize && sizeDescriptions[selectedSize]) {
                const sizeData = sizeDescriptions[selectedSize];
                document.querySelector('.size-info-title').innerHTML = 
                    '📐 ' + sizeData.title;
                document.querySelector('.size-info-desc').innerHTML = 
                    '📝 ' + sizeData.description;
                document.querySelector('.size-info-ideal').innerHTML = 
                    '✔ ' + sizeData.ideal;
                sizeInfo.style.display = 'block';
            } else {
                sizeInfo.style.display = 'none';
            }
        });
    }

    // Form Validation
    const bookingForm = document.querySelector('.booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            if (!this.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            this.classList.add('was-validated');
        });
    }
});
```

---

## 4️⃣ CSS - MODERN STYLING

Complete CSS styling for the booking form:

```css
.booking-container {
    max-width: 900px;
    margin: 2rem auto;
    padding: 0 15px;
}

.booking-header {
    text-align: center;
    margin-bottom: 3rem;
    padding: 2rem 0;
}

.booking-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.booking-subtitle {
    font-size: 1.1rem;
    color: #7f8c8d;
}

.booking-form {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 2px 15px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.form-section {
    border: none;
    padding: 2rem;
    border-bottom: 1px solid #ecf0f1;
}

.form-section:last-of-type {
    border-bottom: none;
}

.section-title {
    display: block;
    font-size: 1.5rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 3px solid #3498db;
}

.form-label {
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.required-badge {
    color: #e74c3c;
    font-weight: bold;
}

.form-control-lg {
    height: 45px;
    padding: 0.75rem 1rem;
    font-size: 1rem;
    border: 2px solid #ecf0f1;
    border-radius: 6px;
    transition: all 0.3s ease;
}

.form-control-lg:focus {
    border-color: #3498db;
    box-shadow: 0 0 0 0.2rem rgba(52, 152, 219, 0.25);
    outline: none;
}

.form-control-lg:hover:not(:focus) {
    border-color: #bdc3c7;
}

textarea.form-control-lg {
    height: auto;
    min-height: 120px;
    resize: vertical;
}

.form-control-file {
    display: block;
    width: 100%;
    padding: 1rem;
    border: 2px dashed #3498db;
    border-radius: 6px;
    background-color: #ecf7ff;
    cursor: pointer;
    transition: all 0.3s ease;
}

.form-control-file:hover {
    border-color: #2980b9;
    background-color: #d9efff;
}

.size-info-box {
    margin-top: 1rem;
    padding: 1rem;
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    border-left: 4px solid #3498db;
    border-radius: 6px;
    animation: slideDown 0.3s ease-out;
}

@keyframes slideDown {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.size-info-title {
    font-weight: 700;
    font-size: 1.1rem;
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.size-info-desc {
    font-size: 0.95rem;
    color: #34495e;
    margin-bottom: 0.5rem;
}

.size-info-ideal {
    font-size: 0.95rem;
    color: #27ae60;
    font-weight: 500;
}

.form-text {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.875rem;
}

.invalid-feedback {
    color: #e74c3c;
    margin-top: 0.25rem;
    font-size: 0.875rem;
}

.form-actions {
    padding: 2rem;
    background: linear-gradient(135deg, #f5f7fa 0%, #ecf0f1 100%);
    border-top: 1px solid #ecf0f1;
}

.booking-submit {
    background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
    border: none;
    font-weight: 600;
    font-size: 1.1rem;
    padding: 1rem 2rem;
    border-radius: 8px;
    transition: all 0.3s ease;
}

.booking-submit:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(52, 152, 219, 0.4);
    background: linear-gradient(135deg, #2980b9 0%, #21618c 100%);
}

.booking-submit:active {
    transform: translateY(0);
}

/* Responsive Design */
@media (max-width: 768px) {
    .booking-title {
        font-size: 1.8rem;
    }

    .booking-subtitle {
        font-size: 1rem;
    }

    .form-section {
        padding: 1.5rem;
    }

    .section-title {
        font-size: 1.25rem;
    }

    .form-control-lg {
        height: 40px;
        font-size: 0.95rem;
    }
}
```

---

## 5️⃣ PYTHON - FORM CONFIGURATION

Simplified form configuration code:

```python
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
            'state': forms.Select(
                choices=INDIAN_STATES,
                attrs={
                    'class': 'form-control form-control-lg',
                    'id': 'stateSelect'
                }
            ),
            # ... more widgets
        }
```

---

## 6️⃣ PYTHON - API ENDPOINT

Backend API for getting cities by state:

```python
@require_http_methods(["GET"])
def get_cities_by_state(request):
    """API endpoint to get cities for a selected state"""
    state = request.GET.get('state', '')
    cities = STATE_CITY_MAP.get(state, [])
    return JsonResponse({'cities': cities})
```

---

## 7️⃣ URL CONFIGURATION

Add this URL pattern to `booking/urls.py`:

```python
path('api/get-cities/', views.get_cities_by_state, name='get_cities'),
```

---

## 8️⃣ DATABASE MIGRATION

Migration to make preferred_date optional:

```python
# booking/migrations/0004_alter_portraitbooking_preferred_date.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_previous_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portraitbooking',
            name='preferred_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
```

---

## 9️⃣ TEMPLATE CONTEXT

Pass this context from views to template:

```python
context = {
    'form': form,
    'state_city_map': json.dumps(STATE_CITY_MAP),
    'size_descriptions': json.dumps(SIZE_DESCRIPTIONS)
}
return render(request, 'booking.html', context)
```

---

## 🔟 TEMPLATE RENDERING

Use in template like this:

```django
{{ form.state }}  <!-- Renders select dropdown -->
{{ form.size }}   <!-- Renders size dropdown with tooltips -->

<script>
    const stateCityMap = {{ state_city_map|safe }};
    const sizeDescriptions = {{ size_descriptions|safe }};
</script>
```

---

## 📌 Quick Copy-Paste References

### Add a New State-City
```python
'New State': ['City1', 'City2', 'City3'],
```

### Add a New Size
```python
'new_size_key': {
    'title': 'Display Title',
    'description': 'Description',
    'ideal': 'Ideal use case'
}
```

### Change Submit Button Color
```css
.booking-submit {
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
}
```

### Adjust Form Width
```css
.booking-container {
    max-width: 1000px; /* Change this value */
}
```

---

## 🧪 Testing Code Snippets

### Test State-City Mapping
```javascript
console.log(stateCityMap['Maharashtra']);
// Output: ["Mumbai", "Pune", "Nagpur", ...]
```

### Test Size Descriptions
```javascript
console.log(sizeDescriptions['8x10']);
// Output: {title: "8\" × 10\"", description: "...", ideal: "..."}
```

### Test Form Submission
```javascript
const form = document.querySelector('.booking-form');
form.submit();
```

---

**Complete code reference - ready to copy and customize!** 💾
