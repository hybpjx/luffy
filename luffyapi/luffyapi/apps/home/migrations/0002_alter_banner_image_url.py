# Generated by Django 3.2.12 on 2022-04-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.ImageField(max_length=255, upload_to='banner', verbose_name='广告图片'),
        ),
    ]
