from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostCreateForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'multiple tags separated by ","'}), required=True)

    class Meta:
        model   = Post
        fields  = ['title', 'content', 'document', 'tags']




class CommentForm(forms.ModelForm):
    
    class Meta:
        model   = Comment
        fields  = ['content']


