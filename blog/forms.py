"""Form for blog page"""
from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    """Display all fields for post form"""
    class Meta:
        """Display all fields for post form"""
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
