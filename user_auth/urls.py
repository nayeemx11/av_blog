from django.urls import path, include
from . import views  # Make sure this imports from the correct app
from blog import views as blog_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.logout, name='logout'),
    path('-signup/', views.signup, name="signup"),
    path('', blog_views.index, name="index"),
]