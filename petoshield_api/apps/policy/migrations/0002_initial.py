# Generated by Django 4.2.6 on 2023-10-29 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprovider',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='policy',
            name='pet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policy', to='pet.pet'),
        ),
        migrations.AddField(
            model_name='insurancecase',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_cases', to='policy.policy'),
        ),
        migrations.AddField(
            model_name='insurancecase',
            name='service_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_cases', to='policy.serviceprovider'),
        ),
        migrations.AddField(
            model_name='incominginvoice',
            name='insurance_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_invoice', to='policy.insurancecase'),
        ),
    ]
