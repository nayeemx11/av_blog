from django.urls import path, include
from . import views
from blog import views as blog_views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('-signup/', views.signup, name="signup"),
    path('', blog_views.index, name="index"),
]

"""
URL configuration for the application.

This module defines the URL patterns for the application, mapping URLs to view functions.

URL patterns:
    - 'login/': Maps to the login_view function for user login.
    - 'logout/': Maps to the logout function for user logout.
    - 'signup/': Maps to the signup function for user registration.
    - '': Maps to the index function from the blog.views module for the homepage.

Includes:
    - 'django.contrib.auth.urls': (Commented out) Includes default authentication URLs for login, logout, and password management.
"""
