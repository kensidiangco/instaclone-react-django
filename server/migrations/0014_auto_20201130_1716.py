# Generated by Django 3.1.3 on 2020-11-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0013_auto_20201130_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=500),
        ),
    ]
