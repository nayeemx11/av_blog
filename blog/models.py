from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    
    """
    Model representing a blog post.

    Fields:
    - title: The title of the post (string).
    - body: The content of the post (text).
    - slug: A unique URL-friendly identifier for the post (slug field).
    - author: The user who authored the post (ForeignKey to User).
    - created: The timestamp when the post was created (datetime).
    - updated: The timestamp when the post was last updated (datetime).
    - status: The publication status of the post (choice field with 'draft' or 'published').
    - image: An optional image for the post (ImageField).
    """
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, related_name="posts_user_to", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='draft')
    image = models.ImageField(upload_to='posts_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    
    """
    Model representing a comment on a post.

    Fields:
    - content: The text content of the comment (text).
    - created: The timestamp when the comment was created (datetime).
    - author: The user who authored the comment (ForeignKey to User).
    - post: The post to which the comment is related (ForeignKey to Post).
    """
    
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_commented", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments_on', on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Replies(models.Model):
    
    """
    Model representing a reply to a comment or another reply.

    Fields:
    - content: The text content of the reply (text).
    - created: The timestamp when the reply was created (datetime).
    - author: The user who authored the reply (ForeignKey to User).
    - comment: The comment to which the reply is related (ForeignKey to Comments, nullable).
    - parent_reply: The reply to which this reply is a child (ForeignKey to self, nullable).
    """
    
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="user_replied", on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments, null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    parent_reply = models.ForeignKey('self', null=True, blank=True, related_name='child_replies', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
