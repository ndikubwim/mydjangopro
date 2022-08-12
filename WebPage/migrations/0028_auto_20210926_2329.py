# Generated by Django 3.2.7 on 2021-09-26 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0027_auto_20210926_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=500)),
                ('Title', models.CharField(max_length=500)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/Courses')),
                ('Course_Content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 23, 29, 17, 932751)),
        ),
        migrations.AlterField(
            model_name='new',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 23, 29, 17, 933751)),
        ),
        migrations.AlterField(
            model_name='posting',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 23, 29, 17, 931720)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 23, 29, 17, 932751)),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.datetime(2021, 9, 26, 23, 29, 17, 928740)),
        ),
    ]