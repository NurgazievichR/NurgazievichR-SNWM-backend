# Generated by Django 5.0.6 on 2024-06-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userti_is_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userti',
            name='is_superuser',
        ),
    ]
