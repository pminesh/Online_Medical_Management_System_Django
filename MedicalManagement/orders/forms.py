from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20,
                                widget=forms.TextInput
                                (attrs={'placeholder': 'Firstname'}))
    last_name = forms.CharField(max_length=20,
                                 widget=forms.TextInput
                                 (attrs={'placeholder': 'Lastname'}))
    email = forms.CharField(max_length=30,
                            widget=forms.EmailInput
                            (attrs={'placeholder': 'Email'}))
    mobile = forms.CharField(max_length=10,
                            widget=forms.TextInput
                            (attrs={'placeholder': 'Mobile'}))
    address = forms.CharField(max_length=30,
                            widget=forms.Textarea
                            (attrs={'placeholder': 'Address'}))
    postal_code = forms.CharField(max_length=6,
                                widget=forms.TextInput
                                (attrs={'placeholder': 'Postal Code'}))
    city = forms.CharField(max_length=20,
                                widget=forms.TextInput
                                (attrs={'placeholder': 'City'}))
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email','mobile', 'address', 'postal_code', 'city']


