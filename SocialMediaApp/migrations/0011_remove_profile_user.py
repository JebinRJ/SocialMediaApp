# Generated by Django 4.1.4 on 2022-12-31 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
