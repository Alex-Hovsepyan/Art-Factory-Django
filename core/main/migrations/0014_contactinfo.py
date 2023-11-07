# Generated by Django 4.2.7 on 2023-11-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_map', models.TextField(verbose_name='Google Map')),
                ('button', models.CharField(max_length=30, verbose_name='Button')),
                ('button_hy', models.CharField(max_length=30, null=True, verbose_name='Button')),
                ('button_en', models.CharField(max_length=30, null=True, verbose_name='Button')),
                ('social1', models.URLField(verbose_name='Social 1')),
                ('social2', models.URLField(verbose_name='Social 2')),
                ('social3', models.URLField(verbose_name='Social 3')),
                ('social4', models.URLField(verbose_name='Social 4')),
                ('social5', models.URLField(verbose_name='Social 5')),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Info',
            },
        ),
    ]
