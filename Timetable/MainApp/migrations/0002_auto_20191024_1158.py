# Generated by Django 2.2.6 on 2019-10-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NLecii', models.CharField(max_length=250)),
                ('Predmet', models.CharField(max_length=250)),
                ('Prepod', models.CharField(max_length=250)),
                ('Podgruppa', models.CharField(max_length=250)),
                ('vremya', models.DateTimeField(auto_now_add=True)),
                ('Auditoriya', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
