from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, EmailInput


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.CharField(widget=EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
