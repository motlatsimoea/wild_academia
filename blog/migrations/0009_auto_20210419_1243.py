# Generated by Django 3.1.4 on 2021-04-19 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210419_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='docs',
            new_name='document',
        ),
    ]
