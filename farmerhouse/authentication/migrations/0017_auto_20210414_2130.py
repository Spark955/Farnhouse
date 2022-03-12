# Generated by Django 3.2 on 2021-04-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_alter_farmer_auth_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader_auth',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='photo',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trader_auth',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]