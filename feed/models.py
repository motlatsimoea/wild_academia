from django.db import models
from accounts.models import MyUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from django.utils.text import slugify
from django.urls import reverse
from blog.models import Tag, Follow


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.feed.author.id, filename)




class Feed(models.Model):
    id 			    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title           = models.CharField(max_length=100, blank=True)
    content         = models.TextField()
    date_posted     = models.DateTimeField(default=timezone.now)
    likes           = models.ManyToManyField(MyUser, related_name='likes', default=None, blank=True)
    author          = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tags            = models.ManyToManyField(Tag, related_name='hashes', default=None, blank=True)

    
    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('feed-detail', kwargs={'pk': self.pk})



class FeedImage(models.Model):
    feed            = models.ForeignKey(Feed, default=None, on_delete=models.CASCADE)
    media           = models.FileField(upload_to=user_directory_path, verbose_name='Media', null=True)

    def __str__(self):
        return self.feed.title



class Opinion(models.Model):
    feed        = models.ForeignKey(Feed, on_delete=models.CASCADE)
    user        = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    reply       = models.ForeignKey('Opinion', null=True, related_name="replies", blank=True, on_delete=models.CASCADE)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return '{}.{}'.format(self.feed.title, str(self.user.username))

    
    def opinion_count(self):
        count = self.count() + self.reply.count()
        return count




LIKE_CHOICES = (
		('Like', 'Like'),
		('Unlike', 'Unlike'),
	)
class Like(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_likes')
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='feed_likes')
	value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

	def __str__(self):
		return str(self.feed)




class Stream(models.Model):
	following 	= models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='stream_following')
	user 		= models.ForeignKey(MyUser, on_delete=models.CASCADE)
	feed 		= models.ForeignKey(Feed, on_delete=models.CASCADE)
	date 		= models.DateTimeField()

	def add_feed(sender, instance, *args, **kwargs):
		feed = instance
		user = feed.author
		followers = Follow.objects.all().filter(following=user)
		for follower in followers:
			stream 	= Stream(feed=feed, user=follower.follower, date=feed.date_posted, following=user)
			stream.save()