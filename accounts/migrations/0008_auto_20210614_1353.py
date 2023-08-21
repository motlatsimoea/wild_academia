# Generated by Django 3.1.4 on 2021-06-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_institute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='group',
            field=models.CharField(choices=[('Student', 'Student'), ('Teacher/Tutor', 'Teacher/Tutor'), ('Mentor', 'Mentor'), ('Mentee', 'Mentee')], max_length=100, verbose_name='select your group'),
        ),
    ]