# Generated by Django 3.1.7 on 2021-04-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_trader_auth_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer_auth',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='trader_auth',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]