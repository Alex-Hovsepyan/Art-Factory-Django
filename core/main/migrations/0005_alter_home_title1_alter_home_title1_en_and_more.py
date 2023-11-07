# Generated by Django 4.2.7 on 2023-11-05 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='title1',
            field=models.CharField(max_length=40, verbose_name='Title 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title1_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Title 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title1_hy',
            field=models.CharField(max_length=40, null=True, verbose_name='Title 1'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title2',
            field=models.CharField(max_length=40, verbose_name='Title 2'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title2_en',
            field=models.CharField(max_length=40, null=True, verbose_name='Title 2'),
        ),
        migrations.AlterField(
            model_name='home',
            name='title2_hy',
            field=models.CharField(max_length=40, null=True, verbose_name='Title 2'),
        ),
    ]
