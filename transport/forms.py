from django import forms
from django.contrib.auth.models import User
from .models import Profile, Order, State


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['origin', 'destination', 'fluid_quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['origin'].queryset = State.objects.all()
        self.fields['destination'].queryset = State.objects.all()

    def clean_fluid_quantity(self):
        fluid_quantity = self.cleaned_data['fluid_quantity']
        if fluid_quantity <= 0:
            raise forms.ValidationError("Fluid quantity must be greater than zero.")
        return fluid_quantity