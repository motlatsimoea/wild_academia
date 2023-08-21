
from django.db import models
from multiselectfield import MultiSelectField
from PIL import Image
from django.urls import reverse



#CREATING CUSTOM USER MODEL
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

USERNAME_REGEX  = '^[a-zA-Z0-9.+-]*$'

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, group, password=None):
        if not username:
            raise ValueError('user must have a username')
        if not email:
            raise ValueError('user must have an email address')

        if not group:
            raise ValueError('Users must have one group')

        user = self.model(
            username    = username,
            email       = email, 
            group       = group

                    
                )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, group, password=None):
        user = self.create_user(
                username, email, group, password=password
            )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
	

    GROUP_CHOICE = (
        ('Student/Mentee', 'Student/Mentee'),
        ('Mentor', 'Mentor'),
        ('Mentor&Teacher', 'Mentor&Teacher'),
        ('Student&Mentor', 'Student&Mentor'),
        ('Mentor&Mentee', 'Mentor&Mentee'),
        
    )

    username = models.CharField(
                    max_length=300,
                    validators = [
                        RegexValidator(regex = USERNAME_REGEX, 
                                        message='Username must be alphanumeric or contain numbers',
                                        code='invalid_username'
                            )],
                    unique=True
                )

    email               = models.EmailField(unique=True)  
    group               = models.CharField(verbose_name='select your group', max_length=100, choices=GROUP_CHOICE)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'group']

    def __str__(self):
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True







class Country(models.Model):
    country     = models.CharField(max_length=100)

    def __str__(self):
        return self.country
        


class District(models.Model):
    district    = models.CharField(max_length=100)

    def __str__(self):
        return self.district


class Township(models.Model):
    township    = models.CharField(max_length=100)

    def __str__(self):
        return self.township



class Profile(models.Model):

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
        ('Computer Coding', 'Computer Coding'),
        ('Business-EDU', 'Business-EDU'),
        ('Career-guidance', 'Career-guidance'),
        ('Medicine', 'Medicine'),
        ('Engineering', 'Engineering'),
        ('Psychology', 'Psychology'),
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Pure Sciences', 'Pure Sciences'),
        ('Finance & Investment', 'Finance & Investment'),
        ('Technical skills', 'Technical skills'),
        ('Farming', 'Farming'),
        ('Arts & Media', 'Arts & Media'),
        ('Leadership Skills', 'Leadership Skills'),

        
    )

    user            = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name      = models.CharField(verbose_name="name", max_length=100, blank=True)
    last_name       = models.CharField(verbose_name="surname", max_length=100, blank=True)
    user_info		= models.TextField(verbose_name='Bio', blank=True)
    image           = models.ImageField(default='default.jpg', upload_to='profile_pics')
    institute       = models.CharField(verbose_name="school/institute", max_length=300, blank=True)
    Subjects        = MultiSelectField(verbose_name='select your Subject(s)', choices=SUBJECT_CHOICE)
    country         = models.CharField(max_length=100, blank=True)
    district        = models.CharField(max_length=100, blank=True)
    township        = models.CharField(max_length=100, blank=True)
    contact			= models.CharField(verbose_name='Contacts', max_length=30, blank=True)

    
    def __str__(self):
        return f'{self.user} Profile'

    def get_absolute_url(self):
        return reverse('profile_details', args=[self.user])

    
    