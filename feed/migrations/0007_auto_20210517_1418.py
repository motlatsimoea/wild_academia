# Generated by Django 3.1.4 on 2021-05-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_remove_comment_likes'),
        ('feed', '0006_auto_20210517_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='hashes', to='blog.Tag'),
        ),
    ]