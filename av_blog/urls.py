from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # adding installed blog app
    path('auth', include('user_auth.urls')), # created app for for authentication purpose
]

# this should be maintained, cause in the released version this will be security issue
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)