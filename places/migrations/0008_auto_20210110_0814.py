# Generated by Django 3.1.1 on 2021-01-10 08:14

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20210110_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='Короткое описание'),
        ),
    ]