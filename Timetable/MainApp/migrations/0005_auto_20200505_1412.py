# Generated by Django 3.0.5 on 2020-05-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20200505_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintable',
            name='NLecii',
            field=models.IntegerField(max_length=250, null=True),
        ),
    ]
