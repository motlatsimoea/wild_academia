# Generated by Django 3.1.4 on 2021-05-21 09:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210521_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Your Answer'),
        ),
    ]
