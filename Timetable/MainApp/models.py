from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class studyPlanPE61(models.Model):
    subject = models.CharField(max_length=250)
    typeSubject = models.CharField(max_length=50)
    hours = models.IntegerField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    remaningLectures = models.IntegerField()


class studyPlanGroup2(models.Model):
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
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class teacher2(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class teacher3(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class teacher4(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


class teacher5(models.Model):
    LessonNumber = models.IntegerField(null=True)
    Date = models.DateField(null=True)
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

    NLecii = models.IntegerField(null=True)
    Predmet = models.CharField(max_length=250, null=True)
    Prepod = models.CharField(max_length=250, null=True)
    Podgruppa = models.CharField(max_length=250, null=True)
    vremya = models.DateField(null=False)
    Auditoriya = models.CharField(max_length=250, null=True)
    teacherId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )


class MainTableGroup2(models.Model):
    NLecii = models.IntegerField(null=True)
    Predmet = models.CharField(max_length=250, null=True)
    Prepod = models.CharField(max_length=250, null=True)
    Podgruppa = models.CharField(max_length=250, null=True)
    vremya = models.DateField(null=False)
    Auditoriya = models.CharField(max_length=250, null=True)
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
