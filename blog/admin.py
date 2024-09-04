from django.contrib import admin
from .models import Post, Comments, Replies

# show inspection in the admin view site
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Replies)