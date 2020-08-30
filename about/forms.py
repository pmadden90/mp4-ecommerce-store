from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tab_title', 'body', 'category', 'header_image') # noqa

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tab_title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tab_title', 'body', 'category', 'header_image') # noqa

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tab_title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),
        }