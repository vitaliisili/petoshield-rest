# Generated by Django 4.2.6 on 2023-10-26 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0002_alter_incominginvoice_insurance_case'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incominginvoice',
            old_name='date',
            new_name='date_test',
        ),
    ]
