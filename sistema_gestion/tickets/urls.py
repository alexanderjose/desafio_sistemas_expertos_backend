from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^listado/$', views.listado_tickets, name='listado_tickets'),
]
