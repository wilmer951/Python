# Generated by Django 5.0.6 on 2024-07-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miappservices', '0003_alter_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]