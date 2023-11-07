# Generated by Django 4.2.7 on 2023-11-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_home_title1_alter_home_title1_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='', verbose_name='Image')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('title_hy', models.CharField(max_length=80, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=80, null=True, verbose_name='Title')),
                ('text1', models.TextField(verbose_name='Text 1')),
                ('text1_hy', models.TextField(null=True, verbose_name='Text 1')),
                ('text1_en', models.TextField(null=True, verbose_name='Text 1')),
                ('colored_part', models.CharField(max_length=80, verbose_name='Colored Part')),
                ('colored_part_hy', models.CharField(max_length=80, null=True, verbose_name='Colored Part')),
                ('colored_part_en', models.CharField(max_length=80, null=True, verbose_name='Colored Part')),
                ('text2', models.TextField(verbose_name='Text 2')),
                ('text2_hy', models.TextField(null=True, verbose_name='Text 2')),
                ('text2_en', models.TextField(null=True, verbose_name='Text 2')),
                ('text3', models.TextField(verbose_name='Text 3')),
                ('text3_hy', models.TextField(null=True, verbose_name='Text 3')),
                ('text3_en', models.TextField(null=True, verbose_name='Text 3')),
                ('button', models.CharField(max_length=30, verbose_name='Button')),
                ('button_hy', models.CharField(max_length=30, null=True, verbose_name='Button')),
                ('button_en', models.CharField(max_length=30, null=True, verbose_name='Button')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
