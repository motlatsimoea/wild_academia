
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Profile, MyUser
from multiselectfield import MultiSelectField

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'
class UserRegistrationsForm(UserCreationForm):

    username    = forms.CharField(
        max_length=30, help_text="Required. Please add valid username"
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'group', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'group', 'email']


class ProfileUpdateForm(forms.ModelForm):
    SUBJECT_CHOICE = (
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('Sesotho', 'Sesotho'),
        ('Physics', 'Physics'),
        ('Chemistry', 'Chemisty'), 
        ('Biology', 'Biology'),
        ('Geograpy', 'Geograpy'),
        ('Accounting', 'Accounting'),
        ('Commerce', 'Commerce'),
        ('French', 'French'),
        ('Coding', 'Coding'),
        ('Business-EDU', 'Business-EDU'),
        ('Career-guidance', 'Career-guidance'),

        
    )

    Subjects = MultiSelectField(verbose_name='select your Subject(s)', choices=SUBJECT_CHOICE)
    class Meta:
        model   = Profile
        fields  = [ 'first_name', 'last_name', 'institute', 'user_info', 'image', 'Subjects', 'country', 'district', 'township', 'contact']
