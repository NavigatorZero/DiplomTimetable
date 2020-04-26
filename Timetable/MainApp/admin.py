from django.contrib import admin


class AcdemicPlan(admin.ModelAdmin):
   list_display = ( 'Group', 'SubjectName',"LectureHours","labHours",
   "PracticeHours",)
   #search_fields = ('Group', 'TeacherFIO')
    #list_filter = ('SubjectName', 'GroupName', 'Auditoriya')
class Tchrs(admin.ModelAdmin):
       list_display = ( 'TeacherFIO', 'Kafedra')


class Grp(admin.ModelAdmin):
    list_display = ( 'GroupName', 'Subgroup')

# admin.site.register(AcademicPlan,AcdemicPlan)
# admin.site.register(Teachers,Tchrs)
# admin.site.register(Cafedra)
# admin.site.register(Auditoriy)
# admin.site.register(Group,Grp)
# admin.site.register(Subject)
