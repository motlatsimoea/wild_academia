# Generated by Django 3.1.4 on 2021-06-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_auto_20210616_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='content',
            field=models.TextField(),
        ),
    ]
