from datetime import date, timedelta

from django.apps import apps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import connection, transaction
from django.db.models import Sum
from django.shortcuts import render

from .Rasp import *
from .models import *


class UserInterface:

    def __init__(self, request):
        self.request = request

    def LessonNumber(self):
        modelName = self.request.user.username
        Model = apps.get_model('MainApp', modelName)
        error = False;

        if self.request.POST.get("userID"):
            return [Model.objects.all(), error]

        if self.request.POST.get("teacherRecordId"):
            Model.objects.filter(id=self.request.POST['teacherRecordId']).delete()
        else:
            if Model.objects.filter(LessonNumber=self.request.POST.get('lessonNumber'),
                                    Date=self.request.POST.get('day')):
                error = True;
            else:
                TeacherLesson = Model()
                TeacherLesson.LessonNumber = self.request.POST['lessonNumber']
                TeacherLesson.Date = self.request.POST['day']
                TeacherLesson.teacher = self.request.user
                TeacherLesson.save()

        return [Model.objects.all(), error]


    def Email(self,variables):
        UserModel = get_user_model()
        user = UserModel.objects.get(email=variables['email'])
        print(user)
        user = authenticate(self.request, username=user, password=variables['password'])

        if user is not None:
            login(self.request, user)
        else:
            print('no Auth')


    def ScheduleDay(self):
        print(self.request.POST['scheduleDay'])
        modelName = self.request.POST['group']
        Model = apps.get_model('MainApp', modelName)

        oneDayRasp = Model.objects.filter(vremya=self.request.POST['scheduleDay'])
        print("anahere")
        return oneDayRasp
