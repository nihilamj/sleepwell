# In forms.py

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import Occupation, HealthProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class OccupationForm(forms.ModelForm):
    class Meta:
        model = Occupation
        fields = ['name']

class HealthProfileSignUPForm(forms.ModelForm):
    #occupation = forms.ModelChoiceField(queryset=Occupation.objects.all(), empty_label=None)

    GENDER_CHOICES = HealthProfile.GENDER_CHOICES

    name = forms.CharField(max_length=255, label='Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(max_length=255, label='Password', required=True, widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', required=True)
    age = forms.IntegerField(label='Age', required=True)
    #occupation = forms.ChoiceField(choices=[(occupation.name, occupation.name) for occupation in Occupation.objects.all()], label='Occupation', required=True)
    occupation = forms.ModelChoiceField(queryset=Occupation.objects.all(), label='Occupation', required=True)

    class Meta:
        model = HealthProfile
        fields = ['name', 'email', 'password', 'gender', 'age', 'occupation']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autocomplete': 'off'})  # To disable autocomplete for email field

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if HealthProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 120:
            raise forms.ValidationError("Age must be between 18 and 120.")
        return age

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(" ".join(e.messages))
        return password


class HealthProfileSignINForm(forms.Form):
    email = forms.EmailField(label="Email", required=True)
    password = forms.CharField(label="Password", max_length=255, required=True, widget=forms.PasswordInput)

    class Meta:
            #model = HealthProfile
            fields = ['email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        print("4")
        if email and password:
            try:
                user = HealthProfile.objects.get(email=email, password=password)
            except HealthProfile.DoesNotExist:
                raise forms.ValidationError("Invalid email or password")
            return cleaned_data