# Generated by Django 3.1.4 on 2021-02-09 05:04

import SocialApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0005_auto_20210205_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialissue',
            name='image',
            field=models.ImageField(upload_to=SocialApp.models.uploads),
        ),
    ]
