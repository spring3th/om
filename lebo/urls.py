from django.conf.urls import include, url
from lebo import views

urlpatterns = [
    url(r'^idc', views.idc, name='idc'),
    url(r'^system',views.system,name='system'),
    url(r'^server',views.server,name='server'),
    url(r'^host',views.host,name='host'),
    url(r'^network',views.network,name='network'),
]
