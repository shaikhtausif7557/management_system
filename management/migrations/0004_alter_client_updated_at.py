# Generated by Django 5.1.1 on 2025-01-20 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_client_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
