# Generated by Django 4.2.6 on 2023-10-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('registration_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('iban', models.CharField(max_length=34)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('policy_number', models.CharField(max_length=255, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('valid', 'Valid'), ('invalid', 'Invalid'), ('expired', 'Expired')], max_length=20)),
                ('initial_limit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('current_limit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('deductible', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='policies', to='pet.pet')),
                ('providers', models.ManyToManyField(related_name='policies', to='policy.serviceprovider')),
            ],
            options={
                'verbose_name_plural': 'policies',
            },
        ),
        migrations.CreateModel(
            name='InsuranceCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('claim_date', models.DateField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('accept', 'Accept'), ('process', 'Process'), ('reject', 'Reject')], default='process', max_length=20)),
                ('service_provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_cases', to='policy.serviceprovider')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IncomingInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('insurance_case', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_invoice', to='policy.insurancecase')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
