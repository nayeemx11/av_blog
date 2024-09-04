from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout, authenticate, login
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm
from .models import UserLoginRecord

def signup(request):
    
    """
    Handles user registration and account creation.

    If the request method is POST, processes the submitted registration form.
    If the form is valid, it saves the new user, displays a success message,
    and redirects to the index page.

    If the request method is GET, initializes a blank registration form.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: The rendered signup template with context including:
            - "form": An instance of CustomUserCreationForm for user registration.
    """
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect(
                "index"
            )  # Redirect to a login page after successful registration
    else:
        form = CustomUserCreationForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):
    
    """
    Handles user login and authentication.

    If the request method is POST, processes the submitted login form.
    If the form is valid, authenticates the user, logs them in, records the login event,
    and redirects to the post list page.

    If the request method is GET, initializes a blank login form.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: The rendered login template with context including:
            - "form": An instance of AuthenticationForm for user login.
    """
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                UserLoginRecord.objects.create(user=user)
                return redirect("post_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


@require_http_methods(["GET", "POST"])
def logout(request):
    
    """
    Handles user logout.

    Logs out the currently authenticated user and redirects to the index page.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: A redirect to the index page.
    """
    
    auth_logout(request)
    return redirect("index")
