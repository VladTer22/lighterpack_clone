from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item, ItemList

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'weight', 'category']

class ItemListForm(forms.ModelForm):
    class Meta:
        model = ItemList
        fields = ['name']

class ShareListForm(forms.ModelForm):
    class Meta:
        model = ItemList
        fields = ['shared_with']
        widgets = {'shared_with': forms.CheckboxSelectMultiple}