from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class studyPlanPE61(models.Model):
    subject = models.CharField(max_length=250)
    typeSubject = models.CharField(max_length=50)
    hours = models.IntegerField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    remaningLectures = models.IntegerField()


class teacher1(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    isBusy = models.BooleanField(default=0)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class teacher2(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    isBusy = models.BooleanField(default=0)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class CafedraClasses(models.Model):
    ClassName = models.CharField(max_length=150)
    AllowedPractice = models.BooleanField(default=0)
    AllowedLabs = models.BooleanField(default=0)
    AllowedLections = models.BooleanField(default=0)


class MainTable(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    NLecii = models.CharField(max_length=250, null=True)
    Predmet = models.CharField(max_length=250, null=True)
    Prepod = models.CharField(max_length=250, null=True)
    Podgruppa = models.CharField(max_length=250, null=True)
    vremya = models.DateTimeField(null=False)
    Auditoriya = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    teacherId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )


class CustomValues(models.Model):
    alias = models.CharField(max_length=250)
    value = models.CharField(max_length=250)


def __str__(self):
    return self.title
