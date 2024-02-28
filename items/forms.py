from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border my-4'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'photo')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'photo': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'photo', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'photo': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }