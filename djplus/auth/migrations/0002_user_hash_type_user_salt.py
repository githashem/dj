# Generated by Django 4.0.3 on 2022-04-30 19:36

from django.db import migrations, models
from django.conf import settings
import djplus.auth.hashers
import djplus.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hash_type',
            field=models.CharField(default=settings.AUTH_DEFAULT_HASHER_NAME, max_length=8),
        ),
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default=djplus.auth.hashers.generate_salt, max_length=32),
        ),
    ]
