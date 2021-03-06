# Generated by Django 3.0.7 on 2020-06-22 15:08

from django.db import migrations, models
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200622_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_bleach.models.BleachField(),
        ),
    ]
