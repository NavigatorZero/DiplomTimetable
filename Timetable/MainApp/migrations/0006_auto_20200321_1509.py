# Generated by Django 3.0.4 on 2020-03-21 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20200321_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintable',
            name='Auditoriya',
            field=models.CharField(default=305, max_length=250),
        ),
        migrations.AlterField(
            model_name='maintable',
            name='NLecii',
            field=models.CharField(default=1, max_length=250),
        ),
        migrations.AlterField(
            model_name='maintable',
            name='Podgruppa',
            field=models.CharField(default='testPoddgruppa', max_length=250),
        ),
        migrations.AlterField(
            model_name='maintable',
            name='Predmet',
            field=models.CharField(default='testSubject', max_length=250),
        ),
        migrations.AlterField(
            model_name='maintable',
            name='Prepod',
            field=models.CharField(default='testTeacher', max_length=250),
        ),
        migrations.AlterField(
            model_name='maintable',
            name='vremya',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 15, 9, 43, 800628)),
        ),
    ]
