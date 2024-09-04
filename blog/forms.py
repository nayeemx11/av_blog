from django import forms
from .models import Post, Comments, Replies

class PostForm(forms.ModelForm):
    
    """
    A form for creating or editing a blog post.

    Linked Model:
    - Post: Represents a blog post.

    Fields:
    - title: The title of the post.
    - body: The main content of the post.
    """
    
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'style': 'width: 25rem; padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;',
                'placeholder': 'Write your Post here...',
            }),
        }


class CommentForm(forms.ModelForm):
    
    """
    A form for creating a comment on a post.

    Linked Model:
    - Comments: Represents a comment on a blog post.

    Fields:
    - content: The text content of the comment.
    """
    
    class Meta:
        model = Comments
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'style': 'width: 25rem; padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;',
                'placeholder': 'Write your comment here...',
            }),
        }

class ReplyForm(forms.ModelForm):
    
    """
    A form for creating a reply to a comment or another reply.

    Linked Model:
    - Replies: Represents a reply to a comment or another reply.

    Fields:
    - content: The text content of the reply.
    """
    
    class Meta:
        model = Replies
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'style': 'width: 25rem; padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc;',
                'placeholder': 'Write your reply here...',
            }),
        }
