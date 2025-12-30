from django import forms
from django.utils.text import slugify

from shop.models import Category, Product


class CategoryForm(forms.ModelForm):
    CATEGORY_CHOICES_WITH_OTHER = Category.CATEGORY_CHOICES + [('other', 'Other (Enter Custom Name)')]

    name = forms.ChoiceField(choices=CATEGORY_CHOICES_WITH_OTHER, label="Category Name")
    custom_name = forms.CharField(max_length=100, required=False, label="Custom Category Name", widget=forms.TextInput(attrs={'placeholder': 'Enter new category name'}))

    class Meta:
        model = Category
        fields = ["description", "image"]
        widgets = {
            "image": forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # For editing existing categories, set the choice to the current name if it's in choices, else 'other'
            if self.instance.name in dict(Category.CATEGORY_CHOICES):
                self.fields['name'].initial = self.instance.name
            else:
                self.fields['name'].initial = 'other'
                self.fields['custom_name'].initial = self.instance.get_name_display()

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        custom_name = cleaned_data.get('custom_name')

        if name == 'other':
            if not custom_name:
                raise forms.ValidationError("Custom category name is required when 'Other' is selected.")
            # Check if custom_name already exists in choices
            existing_names = [choice[0] for choice in Category.CATEGORY_CHOICES]
            if custom_name.lower() in [n.lower() for n in existing_names]:
                raise forms.ValidationError("This category name already exists. Please choose from the dropdown or select a different name.")
            cleaned_data['name'] = custom_name.lower().replace(' ', '_')  # Normalize to match choice format
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        name = self.cleaned_data['name']
        if self.cleaned_data.get('name') == 'other':
            instance.name = self.cleaned_data['custom_name'].lower().replace(' ', '_')
        else:
            instance.name = name
        # Always refresh slug from display name to keep URLs aligned
        instance.slug = slugify(instance.get_name_display())
        if commit:
            instance.save()
        return instance


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "category", "price", "stock"]

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Keep slug in sync with title for clean product URLs, ensuring uniqueness
        base_slug = slugify(instance.title)
        slug = base_slug
        counter = 1
        while Product.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        instance.slug = slug
        if commit:
            instance.save()
        return instance

