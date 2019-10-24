from django.contrib import admin
from .models import MainTable
class PostAdmin(admin.ModelAdmin):
    list_display = ('NLecii', 'Predmet', 'Prepod', 'Podgruppa', 'vremya',"Auditoriya","status")
    search_fields = ('Predmet', 'Prepod')
    list_filter = ('Predmet', 'Auditoriya', 'Prepod')
admin.site.register(MainTable,PostAdmin)
