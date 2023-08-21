# Generated by Django 3.1.4 on 2021-04-06 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('township', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='surname')),
                ('user_info', models.TextField(blank=True, verbose_name='Bio')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Subjects', multiselectfield.db.fields.MultiSelectField(choices=[('Mathematics', 'Mathematics'), ('English', 'English'), ('Sesotho', 'Sesotho'), ('Physics', 'Physics'), ('Chemistry', 'Chemisty'), ('Biology', 'Biology'), ('Geograpy', 'Geograpy'), ('Accounting', 'Accounting'), ('Commerce', 'Commerce'), ('French', 'French'), ('Coding', 'Coding'), ('Business-EDU', 'Business-EDU'), ('Career-guidance', 'Career-guidance')], max_length=125, verbose_name='select your Subject(s)')),
                ('country', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('township', models.CharField(blank=True, max_length=100)),
                ('contact', models.CharField(blank=True, max_length=30, verbose_name='Contacts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
