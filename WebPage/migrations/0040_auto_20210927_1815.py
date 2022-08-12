# Generated by Django 3.2.7 on 2021-09-27 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0039_auto_20210927_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='A_user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 18, 15, 24, 749670)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 18, 15, 24, 754672)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 18, 15, 24, 749670)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 18, 15, 24, 754672)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 27, 18, 15, 24, 749670)),
        ),
    ]