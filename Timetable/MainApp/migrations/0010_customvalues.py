# Generated by Django 3.0.4 on 2020-03-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_auto_20200321_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=250)),
                ('Value', models.CharField(max_length=250)),
            ],
        ),
    ]
