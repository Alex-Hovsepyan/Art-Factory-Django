# Generated by Django 4.2.7 on 2023-11-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_header_lang1_ru_remove_header_lang2_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='header',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='header',
            name='title_hy',
        ),
    ]
