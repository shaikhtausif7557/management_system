# Generated by Django 5.1.1 on 2025-01-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_remove_client_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
