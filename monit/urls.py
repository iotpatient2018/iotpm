from django.conf.urls import include, url
from . import views

urlpatterns=[
		url(r'^$',views.Display_All, name='Display_All'),
]