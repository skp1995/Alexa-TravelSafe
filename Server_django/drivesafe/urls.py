from django.conf.urls import url
from django.contrib import admin

from drivesafe import views


urlpatterns = [

    url(r'^$',views.checkin, name='checkin'),

]