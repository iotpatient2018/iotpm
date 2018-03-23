from django.conf.urls import include, url
from . import views

urlpatterns=[
		url(r'^',views.Ping_Packet, name='Ping_Packet'),
]