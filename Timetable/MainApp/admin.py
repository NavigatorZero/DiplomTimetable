from django.contrib import admin
from .models import AcademicPlan,Teachers,Cafedra,Auditoriy,Group,Subject

#    list_display = ( 'TeacherFIO', 'GroupName',
#    "Auditoriya")
#    search_fields = ('Group', 'TeacherFIO')
#    list_filter = ('SubjectName', 'GroupName', 'Auditoriya')
admin.site.register(AcademicPlan)
admin.site.register(Teachers)
admin.site.register(Cafedra)
admin.site.register(Auditoriy)
admin.site.register(Group)
admin.site.register(Subject)
