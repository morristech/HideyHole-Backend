# Generated by Django 2.1.5 on 2019-03-18 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hideyhole', '0006_auto_20190318_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wallpaper',
            name='image_source_height',
        ),
        migrations.RemoveField(
            model_name='wallpaper',
            name='image_source_width',
        ),
    ]
