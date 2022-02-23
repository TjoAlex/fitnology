"""Form for blog page"""
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    """Display all fields for post form"""
    class Meta:
        """Display all fields for post form"""
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """Display comment"""
    class Meta:
        """Display comment name and body"""
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class':}),
        }
