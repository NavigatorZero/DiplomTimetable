from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.Main_list, name='Main_list'),
    url('Time', views.Time_list, name='Time_list'),
    url('Dif', views.Dif_list, name='Dif_list')
]
