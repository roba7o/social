from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    # method called with is_valid()
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
    
class UserEditForm(forms.ModelForm):
    """
    Allows users to edit their firstname, lastname & email:
    (attributes of the built in django user model
    """
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    """
    Allows users to edit the profile data that is sabved in the custom Profile model
    users can edit DOB and photo
    """
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

