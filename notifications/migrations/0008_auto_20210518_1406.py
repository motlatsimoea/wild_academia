# Generated by Django 3.1.4 on 2021-05-18 12:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20210517_1418'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0020_remove_comment_likes'),
        ('notifications', '0007_delete_notification_feed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification_post',
            new_name='Notification',
        ),
    ]
