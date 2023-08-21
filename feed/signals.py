from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification
from .models import Feed, Opinion, Like, Stream
from blog.models import Follow


@receiver(post_save, sender=Opinion)
def user_opinion_feed(sender, instance, created, **kwargs):
    if created:
        opinion = instance
        feed    = opinion.feed
        sender  = opinion.user
        if sender != feed.author:
            notify = Notification(feed=feed, sender=sender, user=feed.author, notification_type=4)
            notify.save()

        if opinion.reply is not None:
            notify_opinion_owner = Notification(feed=feed, sender=sender, user=opinion.reply.user, notification_type=5)
            notify_opinion_owner.save()


@receiver(post_save, sender=Like)
def user_liked_feed(sender, instance, created, **kwargs):
    if created:
        like 	= instance
        feed 	= like.feed
        sender 	= like.user
        notify 	= Notification(feed=feed, sender=sender, user=feed.author, notification_type=1)
        notify.save()




@receiver(post_save, sender=Feed)
def add_post(sender, instance, created, **kwargs):
    if created:
        feed = instance
        user = feed.author
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            stream 	= Stream(feed=feed, user=follower.follower, date=feed.date_posted, following=user)
            stream.save()

