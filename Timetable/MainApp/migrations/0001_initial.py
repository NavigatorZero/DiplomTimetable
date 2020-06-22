# Generated by Django 3.0.3 on 2020-02-23 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CafedraClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassName', models.CharField(max_length=150)),
                ('AllowedPractice', models.BooleanField(default=0)),
                ('AllowedLabs', models.BooleanField(default=0)),
                ('AllowedLections', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NLecii', models.CharField(max_length=250)),
                ('Predmet', models.CharField(max_length=250)),
                ('Prepod', models.CharField(max_length=250)),
                ('Podgruppa', models.CharField(max_length=250)),
                ('vremya', models.DateTimeField()),
                ('Auditoriya', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='teacher2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LessonNumber', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('isBusy', models.BooleanField(default=0)),
                ('teache', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='teacher1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LessonNumber', models.IntegerField(null=True)),
                ('Date', models.DateField(null=True)),
                ('isBusy', models.BooleanField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='studyPlanPE61',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('typeSubject', models.CharField(max_length=50)),
                ('hours', models.IntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
