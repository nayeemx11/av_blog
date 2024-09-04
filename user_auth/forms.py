from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    
    """
    A custom user creation form that extends Django's built-in UserCreationForm.

    This form is used for creating new user accounts with additional email field. 
    It ensures that the email field is required and validates the provided email address.

    Fields:
        username (str): The username for the new user.
        email (str): The email address of the new user.
        password1 (str): The password for the new user.
        password2 (str): The confirmation of the new user's password.

    Methods:
        save(commit=True):
            Saves the user instance to the database, including the email address.
            If `commit` is True, the user instance is saved to the database.

    Args:
        commit (bool): A boolean indicating whether to save the user instance to the database.

    Returns:
        User: The saved user instance.
    """
    
    email = forms.EmailField(
        required=True, help_text="Required. Enter valid email address."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    
    """
    A custom user login form that extends Django's built-in AuthenticationForm.

    This form is used for user authentication, allowing users to log in with their username and password.

    Fields:
        username (str): The username of the user.
        password (str): The password for the user.

    Args:
        None

    Returns:
        AuthenticationForm: An instance of AuthenticationForm for user login.
    """
    
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
