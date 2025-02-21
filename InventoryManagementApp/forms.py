from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InventoryItemForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()  # Fetch fresh categories
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),  # Avoid stale data
        empty_label="Select Category"  # Optional placeholder
    )

    class Meta:
        model = InventoryItem
        fields = ['brand', 'code', 'price', 'size', 'type', 'quantity', 'category']
