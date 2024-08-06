from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['heading_text', 'message_text']
    
    heading_text = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your title...',
            'maxlength': '60'
        }),
        error_messages={'max_length': 'Title cannot exceed 60 characters.'}
    )
    
    message_text = forms.CharField(
        max_length=280,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter your message...',
            'maxlength': '280'
        }),
        error_messages={'max_length': 'Message cannot exceed 280 characters.'}
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments_text']