# Generated by Django 2.2.6 on 2019-12-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_studyplanpe61_studyplanpe71'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyplanpe61',
            name='hours',
            field=models.DecimalField(decimal_places=1, max_digits=10),
        ),
    ]
