# Generated by Django 3.2.7 on 2021-09-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebPage', '0015_alter_student_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.CharField(max_length=500),
        ),
    ]