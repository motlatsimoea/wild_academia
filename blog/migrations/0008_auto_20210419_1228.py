# Generated by Django 3.1.4 on 2021-04-19 10:28

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210413_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to=blog.models.user_directory_path),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
