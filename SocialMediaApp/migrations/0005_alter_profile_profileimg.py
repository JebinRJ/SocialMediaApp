# Generated by Django 4.1.4 on 2022-12-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0004_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='17004.png', upload_to='profile_images'),
        ),
    ]
