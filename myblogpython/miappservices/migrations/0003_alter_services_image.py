# Generated by Django 5.0.6 on 2024-07-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miappservices', '0002_rename_servicios_services_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='servicesapp'),
        ),
    ]
