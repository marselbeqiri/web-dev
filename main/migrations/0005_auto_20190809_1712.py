# Generated by Django 2.2.3 on 2019-08-09 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190805_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='tuttorial_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images_main/'),
        ),
        migrations.AddField(
            model_name='tutorialcategory',
            name='category_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images_main/'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 9, 17, 12, 54, 495453), verbose_name='Date published'),
        ),
    ]
