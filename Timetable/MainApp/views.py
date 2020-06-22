from datetime import date, timedelta

from django.apps import apps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import connection, transaction
from django.db.models import Sum
from django.shortcuts import render
from . import UserInterface
from . import TablePreparation

from .Rasp import *
from .models import *



def Main_list(request):
    if request.method == 'POST':
        preparations= TablePreparation.TablePreparation()
        interface = UserInterface.UserInterface(request)

        variables = request.POST

        if request.POST.get("lessonNumber") or request.POST.get("teacherRecordId") or request.POST.get("userID"):
            teacherTable = interface.LessonNumber()
            return render(request, 'modal_table.html', {"teacherTable": teacherTable[0], "error": teacherTable[1]}, )

        if 'email' in variables:
            interface.Email(variables)

        if 'logout' in variables:
            logout(request)

        if request.method == 'POST' and 'scheduleDay' in request.POST:
            oneDayRasp = interface.ScheduleDay()
            return render(request, 'main_table.html',
                          {'posts': oneDayRasp, 'dayRasp': request.POST['scheduleDay']})

        if 'erase' in variables:
            preparations.Erase()

        if 'fill' in variables:
            preparations.Fill()
            # cursor = connection.cursor()
            # # Data modifying operation - commit required
            # # cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'MainApp_maintable'")
            # # transaction.commit()

    Result = MainTable.objects.all()

    return render(request, 'test.html', {'posts': Result, })

def Time_list(request):
    return render(request, 'Time.html')

def Dif_list(request):
    return render(request, 'dif.html')
        
