# Generated by Django 3.1.4 on 2021-05-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20210504_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.IntegerField(choices=[(1, 'Like'), (2, 'Comment'), (3, 'Follow')]),
        ),
    ]
