# Generated by Django 3.1.4 on 2021-02-05 06:46

import SocialApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0004_auto_20210204_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=SocialApp.models.uploads),
        ),
        migrations.AlterField(
            model_name='socialissue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=SocialApp.models.uploads),
        ),
    ]
