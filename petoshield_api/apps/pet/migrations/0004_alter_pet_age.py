# Generated by Django 4.2.6 on 2023-11-06 14:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0003_alter_breed_risk_level_alter_pet_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="age",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(20),
                ]
            ),
        ),
    ]
