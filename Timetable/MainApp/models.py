from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class AcademicPlan(models.Model):
    Group=models.CharField(max_length=45, primary_key=True)
    SubjectName=models.CharField(max_length=100)
    LectureHours=models.IntegerField()
    labHours=models.IntegerField()
    PracticeHours=models.IntegerField()


class Teachers(models.Model):
    TeacherFIO=models.CharField(max_length=100, primary_key=True)
    Kafedra=models.CharField(max_length=100)


class Cafedra (models.Model):
    CafedraName=models.CharField(max_length=100, primary_key=True)


class Auditoriy(models.Model):
    AuditoriyType=[
    ("Лабораторная","Лабораторная"),
    ("Практическая","Практическая"),
    ( "Лекционная","Лекционная")]  #Обдумать
    type=models.CharField(max_length=45,choices=AuditoriyType)
    Additionaltype=models.CharField(max_length=45,choices=AuditoriyType)
    Kafedra=models.CharField(max_length=45)
    Auditoriyname=models.IntegerField()


class Group(models.Model):
    GroupName=models.CharField(max_length=45, primary_key=True)
    Subgroup=models.IntegerField()


class Subject(models.Model):
    idSubj=models.IntegerField()
    idAudit=models.IntegerField()
    SubjectType=models.IntegerField()
    Group=models.IntegerField()
    Subgroup=models.IntegerField()
    TeacherFIO=models.IntegerField()
    Subject=models.IntegerField()
    SubjectNumber=models.IntegerField()
    Date=models.IntegerField()







class MainTable(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    NLecii = models.CharField(max_length=250)
    Predmet = models.CharField(max_length=250)

    Prepod =   models.CharField(max_length=250)
    Podgruppa = models.CharField(max_length=250)
    vremya= models.DateTimeField(auto_now_add=True)
    Auditoriya =  models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title


class Another_group(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    NLecii = models.CharField(max_length=250)
    Predmet = models.CharField(max_length=250)

    Prepod =   models.CharField(max_length=250)
    Podgruppa = models.CharField(max_length=250)
    vremya= models.DateTimeField(auto_now_add=True)
    Auditoriya =  models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
