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
                        obj.teacherId = PrepodTable[y].teacher
                        obj.save()

    # функция устанавливает предмет в главную таблицу
    def setSubject(Table, studyPlan, hours):
        Table.exclude(Prepod="")

        for x in range(len(Table)):
            for y in range(len(studyPlan)):
                if Table[x].teacherId == studyPlan[y].teacher and hours > 0:
                    obj = MainTable.objects.get(pk=Table[x].id)
                    hoursType = studyPlan[y].hours
                    if studyPlan[y].typeSubject == "Лекция" and obj.Auditoriya == "" and  studyPlan[y].remaningLectures > 0 :
                        clases = CafedraClasses.objects.filter(AllowedLections="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue

                    if studyPlan[y].typeSubject == "Практика" and obj.Auditoriya == "" and studyPlan[y].remaningLectures > 0:
                        clases = CafedraClasses.objects.filter(AllowedPractice="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue

                    if studyPlan[y].typeSubject == "ЛабРабота" and obj.Auditoriya == "" and studyPlan[y].remaningLectures > 0:
                        clases = CafedraClasses.objects.filter(AllowedLabs="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()

                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue
