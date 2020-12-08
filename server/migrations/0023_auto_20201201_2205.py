# Generated by Django 3.1.3 on 2020-12-01 14:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0022_auto_20201201_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]