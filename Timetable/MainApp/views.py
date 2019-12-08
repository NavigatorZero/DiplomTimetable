from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MainTable,Prepod1,studyPlanPE61
from django.db.models import Sum,Max,Count,Avg






class Rasp():
       
        def setTeacher(Table,PrepodTable):
                for x in range(len(Table)):  
                        for y in range(len(PrepodTable)):
                                if Table[x].id==PrepodTable[y].id:
                                        obj = MainTable.objects.get(pk=Table[x].id)
                                        obj.Prepod = "Уймин А.Г"#надо откуда то брать имя препода
                                        obj.NLecii =PrepodTable[y].LessonNumber
                                        obj.vremya = PrepodTable[y].Date
                                        obj.save()

        def setSubject(Table,studyPlan):
                for x in range(len(Table)):
                        for y in range(len(studyPlan)):
                                if Table[x].Prepod!="" and Table[x].Prepod in studyPlan[y].teacher:
                                        subjectHours=studyPlan[y].hours
                                        obj = MainTable.objects.get(pk=Table[x].id)
                                        obj.Predmet=studyPlan[y].subject
                                        obj.save()
                                        subjectHours=subjectHours-1
                                        print(subjectHours)
              
       
        




def Main_list(request):
        semestrdays=121#кол-во дней в семестре
        semestrHours=726 #часов в семестре
        AllHours=studyPlanPE61.objects.aggregate(Sum('hours'))#кол-во часов одной группы в семестр по всем дисциплинам
        HoursByDiscipline=studyPlanPE61.objects.aggregate(Sum('hours'))

        group1=studyPlanPE61.objects.all()
        Academic=MainTable.objects.all()
        prepodAray=Prepod1.objects.filter(isBusy="True")
     
        Rasp.setTeacher(Academic,prepodAray) 
        Rasp.setSubject(Academic,group1) 
        return render(request, 'test.html', {'posts': Academic,"groups":prepodAray,"tests":AllHours, })
