# Generated by Django 4.2.7 on 2023-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='About2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('title_hy', models.CharField(max_length=80, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=80, null=True, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_hy', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'About 2',
                'verbose_name_plural': 'About 2',
            },
        ),
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('title_hy', models.CharField(max_length=60, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=60, null=True, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_hy', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
            ],
        ),
    ]
