from django.db import models
from accounts.models import MyUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Category(models.Model):
    title   = models.CharField(max_length=100)
    slug    = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Label(models.Model):
    title       = models.CharField(max_length=100, verbose_name='Label')
    slug        = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title           = models.CharField(max_length=100, blank=True)
    slug            = models.SlugField(unique=True, default=None)
    status          = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10, verbose_name='status')
    content         = RichTextUploadingField()
    date_posted     = models.DateTimeField(default=timezone.now)
    category        = models.ForeignKey(Category, verbose_name='Category', default='general', on_delete=models.CASCADE)
    picture         = models.ImageField(upload_to='articles/%Y/%m/%d', default=None)
    author          = models.CharField(max_length=150, blank=False)
    tags            = models.ManyToManyField(Label)


    
    def __str__(self):
        return self.title
