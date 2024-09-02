from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('index')  # Redirect to a login page after successful registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})



@require_http_methods(["GET", "POST"])
def logout(request):
    auth_logout(request)
    return redirect('index')