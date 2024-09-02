from django import forms
from .models import Post, Comments, Replies

class PostForm(forms.ModelForm):
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
