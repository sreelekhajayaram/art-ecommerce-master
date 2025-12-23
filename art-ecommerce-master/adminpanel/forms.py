from django import forms
from django.utils.text import slugify

from shop.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description", "image"]
        widgets = {
            "image": forms.ClearableFileInput(),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
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
        # Keep slug in sync with title for clean product URLs
        instance.slug = slugify(instance.title)
        if commit:
            instance.save()
        return instance

