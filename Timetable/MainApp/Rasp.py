from .models import MainTable
from .models import MainTable, CafedraClasses


class Rasp:

    # Функция устанавливает в главную таблицу преподователей
    def setTeacher(Table, PrepodArray):
        for x in range(len(Table)):
            for PrepodTable in PrepodArray:
                for y in range(len(PrepodTable)):
                    if Table[x].id == PrepodTable[y].id and Table[x].Prepod == "":
                        obj = MainTable.objects.get(pk=Table[x].id)
                        obj.Prepod = PrepodTable[y].teacher.last_name + " " + PrepodTable[
                            y].teacher.first_name  # надо откуда то брать имя препода
                        obj.NLecii = PrepodTable[y].LessonNumber
                        obj.vremya = PrepodTable[y].Date
                        obj.save()

    # функция устанавливает предмет в главную таблицу
    def setSubject(Table, studyPlan, hours):
        Table.exclude(Prepod="")

        for x in range(len(Table)):
            print(hours)
            for y in range(len(studyPlan)):

                test = studyPlan[y].teacher.last_name + " " + studyPlan[y].teacher.first_name
                if Table[x].Prepod == test and hours>0:
                    obj = MainTable.objects.get(pk=Table[x].id)
                    obj.Predmet = studyPlan[y].subject
                    if studyPlan[y].typeSubject == "Лекция" and Table[x].Auditoriya == "":
                        clases = CafedraClasses.objects.filter(AllowedLections="True")
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        hours-=1
                        continue

                    elif studyPlan[y].typeSubject == "Практика" and Table[x].Auditoriya == "":
                        clases = CafedraClasses.objects.filter(AllowedPractice="True")
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        hours-=1
                        continue

                    elif studyPlan[y].typeSubject == "ЛабРабота" and Table[x].Auditoriya == "":
                        clases = CafedraClasses.objects.filter(AllowedLabs="True")
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        hours-=1
                        continue
