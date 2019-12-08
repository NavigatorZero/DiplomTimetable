from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class studyPlanPE61(models.Model):
    subject=models.CharField(max_length=250)
    typeSubject=models.CharField(max_length=50)
    hours=models.IntegerField()
    teacher=models.CharField(max_length=150)

class studyPlanPE71(models.Model):
    subject=models.CharField(max_length=250)
    typeSubject=models.CharField(max_length=50)
    hours=models.IntegerField(null=False)
    teacher=models.CharField(max_length=150)
class Prepod1(models.Model):
    LessonNumber=models.IntegerField(null=True)
    Date=models.DateField(null=True)
    isBusy=models.BooleanField(default=0)

class Prepod2(models.Model):
    LessonNumber=models.IntegerField(null=True)
    Date=models.DateField(null=True)
    isBusy=models.BooleanField(default=0)
class MainTable(models.Model):
        STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
        )
        NLecii = models.CharField(max_length=250)
        Predmet = models.CharField(max_length=250)
        Prepod =   models.CharField(max_length=250)
        Podgruppa = models.CharField(max_length=250)
        vremya= models.DateTimeField()
        Auditoriya =  models.CharField(max_length=250)
        status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

   

def __str__(self):
    return self.title



