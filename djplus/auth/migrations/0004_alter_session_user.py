# Generated by Django 4.0.5 on 2022-07-20 14:43

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0003_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
