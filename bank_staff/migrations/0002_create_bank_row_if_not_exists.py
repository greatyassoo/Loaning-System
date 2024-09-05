# Generated by Django 5.1 on 2024-09-05 15:20

from django.db import migrations, models


def create_single_bank_instance(apps, schema_editor):
    bank = apps.get_model('bank_staff', 'Bank')
    if not bank.objects.exists():
        bank.objects.create(total_funds=0)


class Migration(migrations.Migration):

    dependencies = [
        ('bank_staff', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_single_bank_instance),
    ]
