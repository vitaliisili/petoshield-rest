# Generated by Django 4.2.6 on 2023-11-14 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_mailverificationtokens_redirect_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailverificationtokens',
            name='redirect_link',
            field=models.URLField(),
        ),
    ]
