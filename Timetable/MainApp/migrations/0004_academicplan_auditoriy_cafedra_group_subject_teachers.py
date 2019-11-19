# Generated by Django 2.2.6 on 2019-11-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_another_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicPlan',
            fields=[
                ('Group', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('SubjectName', models.CharField(max_length=100)),
                ('LectureHours', models.IntegerField()),
                ('labHours', models.IntegerField()),
                ('PracticeHours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Auditoriy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Лабораторная', 'Лабораторная'), ('Практическая', 'Практическая'), ('Лекционная', 'Лекционная')], max_length=45)),
                ('Additionaltype', models.CharField(choices=[('Лабораторная', 'Лабораторная'), ('Практическая', 'Практическая'), ('Лекционная', 'Лекционная')], max_length=45)),
                ('Kafedra', models.CharField(max_length=45)),
                ('Auditoriyname', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cafedra',
            fields=[
                ('CafedraName', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('GroupName', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('Subgroup', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSubj', models.IntegerField()),
                ('idAudit', models.IntegerField()),
                ('SubjectType', models.IntegerField()),
                ('Group', models.IntegerField()),
                ('Subgroup', models.IntegerField()),
                ('TeacherFIO', models.IntegerField()),
                ('Subject', models.IntegerField()),
                ('SubjectNumber', models.IntegerField()),
                ('Date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('TeacherFIO', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Kafedra', models.CharField(max_length=100)),
            ],
        ),
    ]