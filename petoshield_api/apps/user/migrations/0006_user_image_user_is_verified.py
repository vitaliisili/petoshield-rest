# Generated by Django 4.2.6 on 2023-11-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_mailverificationtokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pictures'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]