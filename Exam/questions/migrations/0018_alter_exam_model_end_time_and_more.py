# Generated by Django 4.2.7 on 2023-11-25 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0017_merge_20210127_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 22, 50, 36, 234906)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 22, 50, 36, 234906)),
        ),
    ]
