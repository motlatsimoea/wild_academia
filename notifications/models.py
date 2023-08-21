from django.db import models
from accounts.models import MyUser


class Notification(models.Model):
	NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'), (4, 'Opinion'), (5, 'Reply'))

	post 				= models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='noti_post', blank=True, null=True)
	feed 				= models.ForeignKey('feed.Feed', on_delete=models.CASCADE, related_name='noti_feed', blank=True, null=True)
	sender 				= models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='noti_from_user')
	user 				= models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='noti_to_user')
	notification_type 	= models.IntegerField(choices=NOTIFICATION_TYPES)
	text_preview 		= models.CharField(max_length=50, blank=True)
	date 				= models.DateTimeField(auto_now_add=True)
	is_seen 			= models.BooleanField(default=False)
