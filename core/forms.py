from django import forms
from core.models import User
from registration.forms import RegistrationForm
from django.contrib.auth import get_user_model, authenticate, password_validation
from django.contrib.auth.models import Group
    # https://docs.djangoproject.com/en/2.2/topics/auth/default/#groups

User = get_user_model()

class EditProfileForm(forms.Form):
    name = forms.CharField(
        label= 'Name',
        max_length=100,
        widget=forms.TextInput(attrs={'required': True})
    )

class CustomRegistrationForm(RegistrationForm):
    # https://github.com/macropin/django-registration/blob/master/registration/forms.py
    # https://github.com/django/django/blob/master/django/contrib/auth/forms.py

    email = forms.EmailField(
        label='E-mail', 
        widget=forms.TextInput(attrs={'class': ''}),
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': ''}),
        # help_text=password_validation.password_validators_help_text_html(),
        help_text=None,
    )

    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'class': ''}),
        strip=False,
        help_text="Enter the same password as before, for verification.",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = None

    class Meta(RegistrationForm.Meta): # Meta is a class defined in a class
        
        widgets = {
            'username': forms.TextInput(attrs={'class': ''}),
        }

class NewGroupForm(forms.Form):

    name = forms.CharField(label='Name',
        max_length=512,
        widget=forms.TextInput(attrs={'placeholder': 'enter a group name'})
    )
    def save(self, **kwargs):
        if self.is_valid():
            group_properties = {'name': self.cleaned_data['name']}
            group_properties.update(kwargs)
            return Group.objects.create(**group_properties)
        return None
