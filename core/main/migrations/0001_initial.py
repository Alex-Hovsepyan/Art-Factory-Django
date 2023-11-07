# Generated by Django 4.2.7 on 2023-11-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Title')),
                ('title_hy', models.CharField(max_length=40, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=40, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=40, null=True, verbose_name='Title')),
                ('path1', models.CharField(max_length=40, verbose_name='Path 1')),
                ('path1_hy', models.CharField(max_length=40, null=True, verbose_name='Path 1')),
                ('path1_ru', models.CharField(max_length=40, null=True, verbose_name='Path 1')),
                ('path1_en', models.CharField(max_length=40, null=True, verbose_name='Path 1')),
                ('path2', models.CharField(max_length=40, verbose_name='Path 2')),
                ('path2_hy', models.CharField(max_length=40, null=True, verbose_name='Path 2')),
                ('path2_ru', models.CharField(max_length=40, null=True, verbose_name='Path 2')),
                ('path2_en', models.CharField(max_length=40, null=True, verbose_name='Path 2')),
                ('path3', models.CharField(max_length=40, verbose_name='Path 3')),
                ('path3_hy', models.CharField(max_length=40, null=True, verbose_name='Path 3')),
                ('path3_ru', models.CharField(max_length=40, null=True, verbose_name='Path 3')),
                ('path3_en', models.CharField(max_length=40, null=True, verbose_name='Path 3')),
                ('path4', models.CharField(max_length=40, verbose_name='Path 4')),
                ('path4_hy', models.CharField(max_length=40, null=True, verbose_name='Path 4')),
                ('path4_ru', models.CharField(max_length=40, null=True, verbose_name='Path 4')),
                ('path4_en', models.CharField(max_length=40, null=True, verbose_name='Path 4')),
                ('path5', models.CharField(max_length=40, verbose_name='Path 5')),
                ('path5_hy', models.CharField(max_length=40, null=True, verbose_name='Path 5')),
                ('path5_ru', models.CharField(max_length=40, null=True, verbose_name='Path 5')),
                ('path5_en', models.CharField(max_length=40, null=True, verbose_name='Path 5')),
                ('lang1', models.CharField(max_length=5, verbose_name='Language 1')),
                ('lang1_hy', models.CharField(max_length=5, null=True, verbose_name='Language 1')),
                ('lang1_ru', models.CharField(max_length=5, null=True, verbose_name='Language 1')),
                ('lang1_en', models.CharField(max_length=5, null=True, verbose_name='Language 1')),
                ('lang2', models.CharField(max_length=5, verbose_name='Language 2')),
                ('lang2_hy', models.CharField(max_length=5, null=True, verbose_name='Language 2')),
                ('lang2_ru', models.CharField(max_length=5, null=True, verbose_name='Language 2')),
                ('lang2_en', models.CharField(max_length=5, null=True, verbose_name='Language 2')),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
    ]