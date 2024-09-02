from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey(User, related_name="posts_user_to", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class Comments(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_commented", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments_on', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Replies(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_replied", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    parent_reply = models.ForeignKey('self', null=True, blank=True, related_name='child_replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
