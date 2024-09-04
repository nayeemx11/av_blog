from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # adding installed blog app
    path('auth', include('user_auth.urls')), # created app for for authentication purpose
]
