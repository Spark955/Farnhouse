# Generated by Django 3.2 on 2021-04-21 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0004_crops_image_link'),
        ('traders', '0003_auto_20210421_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='crops_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='farmers.crops'),
        ),
    ]
