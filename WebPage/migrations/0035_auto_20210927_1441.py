# Generated by Django 3.2.7 on 2021-09-27 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0034_auto_20210927_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 14, 41, 58, 276115)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 14, 41, 58, 276115)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 14, 41, 58, 276115)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 14, 41, 58, 276115)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 14, 41, 58, 276115)),
        ),
    ]
