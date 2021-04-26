from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from apps.dealers.models import Dealer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, max_length=128, label='Password')
    remember_me = forms.BooleanField(required=False, initial=False, label='Remember me')

    def clean(self):
        cleaned_data = super().clean()

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError('User not found')

        self.cleaned_data['user'] = user


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Username')
    email = forms.CharField(widget=forms.EmailInput, max_length=30, label='Email')

    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    # password_confirm = forms.CharField(widget=forms.PasswordInput, validators=[validate_password])
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Dealer
        fields = ("username", "password", 'email', 'first_name', 'last_name', 'title')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if not user:
            raise ValidationError('User not found')

        self.cleaned_data['user'] = user

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean_password_confirm(self):
        password = self.cleaned_data['password_confirm']

        if password != self.cleaned_data['password']:
            raise ValidationError("Passwords didn't match", code='invalid_passwords')
        return password