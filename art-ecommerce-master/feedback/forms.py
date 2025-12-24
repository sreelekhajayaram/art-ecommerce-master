from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'your@email.com',
                'required': True,
                'readonly': True
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Share your experience and feedback...',
                'rows': 5,
                'required': True
            }),
            'rating': forms.RadioSelect(choices=Feedback.RATING_CHOICES, attrs={
                'class': 'form-check-input rating-input'
            })
        }
        labels = {
            'name': 'Your Name',
            'email': 'Email Address',
            'comment': 'Your Feedback',
            'rating': 'Rating'
        }
