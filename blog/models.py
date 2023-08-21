from django.db import models
from accounts.models import MyUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
from django.urls import reverse
from notifications.models import Notification



def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.author.username, filename)


class Tag(models.Model):
    title       = models.CharField(max_length=100, verbose_name='Tag')
    slug        = models.SlugField( max_length=150, null=False, unique=True)
    

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

        

class Post(models.Model):
    id 			    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title           = models.CharField(max_length=100, blank=True)
    content         = RichTextUploadingField()
    document        = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    date_posted     = models.DateTimeField(default=timezone.now)
    author          = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tags            = models.ManyToManyField(Tag, related_name='tags')


    
    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    



class Comment(models.Model):
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    user        = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content     = RichTextUploadingField( verbose_name='Your Answer')
    timestamp   = models.DateTimeField(auto_now_add=True)


    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return '{}.{}'.format(self.post.title, str(self.user.username))



class Follow(models.Model):
    follower        = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='follower')
    following        = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='following')

    def user_follow(sender, instance, *args, **kwargs):
        follow      = instance
        sender      = follow.follower
        following   = follow.following

        notify      = Notification(sender=sender, user=following, notification_type=3)
        notify.save()

    def user_unfollow(sender, instance, *args, **kwargs):
        follow      = instance
        sender      = follow.follower
        following   = follow.following

        notify      = Notification.objects.filter(sender=sender, user=following, notification_type=3)
        notify.delete()











