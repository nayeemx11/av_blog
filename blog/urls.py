from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post_list/', views.post_list, name="post_list"),
    path('post_detail_view/<int:id>/', views.post_detail_view, name="post_detail_view")
]

"""
URL configuration for the blog application.

This module defines the URL patterns for the blog app. Each pattern maps a URL path
to a specific view function in the `views` module. 

URL Patterns:
1. `''` (Root URL): 
   - View: `views.index`
   - Name: `index`
   - Description: Displays the index or home page of the blog application.

2. `'post_list/'`: 
   - View: `views.post_list`
   - Name: `post_list`
   - Description: Displays a list of all blog posts. Also handles form submission 
        for creating new posts.

3. `'post_detail_view/<int:id>/'`: 
   - View: `views.post_detail_view`
   - Name: `post_detail_view`
   - Description: Displays detailed information about a specific blog post. The `id` 
        parameter in the URL is used to identify which post to display.

Each URL pattern uses the `path()` function from Django's `urls` module to map 
URL paths to view functions. The `name` argument provides a unique name for each 
URL pattern, which can be used to refer to these URLs in templates and other 
parts of the code.

"""