# Generated by Django 3.0.5 on 2020-05-03 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LessonNumber', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('isBusy', models.BooleanField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LessonNumber', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('isBusy', models.BooleanField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LessonNumber', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('isBusy', models.BooleanField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='teacher',
        ),
    ]