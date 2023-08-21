# Generated by Django 3.1.4 on 2021-05-17 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_delete_stream'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0004_stream'),
        ('notifications', '0004_auto_20210513_2006'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notification_post',
        ),
        migrations.CreateModel(
            name='Notification_feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.IntegerField(choices=[(1, 'Like'), (2, 'Comment'), (3, 'Follow'), (4, 'Opinion'), (5, 'Reply')])),
                ('text_preview', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_seen', models.BooleanField(default=False)),
                ('feed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noti_feed', to='feed.feed')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_from_feed_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noti_to_feed_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]