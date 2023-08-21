from django import forms
from .models import Opinion

class OpinionForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a reply...', 'rows':'4', 'cols':'50'}))
    class Meta:
        model   = Opinion
        fields  = ['content']