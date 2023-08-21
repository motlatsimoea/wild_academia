from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Follow
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def user_comment_post(sender, instance, created, **kwargs):
    if created:
        comment = instance
        post = comment.post
        sender = comment.user
        if sender != post.author:
            notify = Notification(post=post, sender=sender, user=post.author, notification_type=2)
            notify.save()


        for comment in post.comment_set.all():
            if comment.user != sender:
                notify_participants = Notification(post=post, sender=sender, user=comment.user, notification_type=2)
                notify_participants.save()



@receiver(post_save, sender=Follow)
def user_follow(sender, instance, created, **kwargs):
    if created:
        follow      = instance
        sender      = follow.follower
        following   = follow.following
        notify      = Notification(sender=sender, user=following, notification_type=3)
        notify.save()
