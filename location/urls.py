#app/urls.py file

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    #re_path('^(?P<s1>[0-9]+).(?P<s2>[0-9]+).(?P<s3>[0-9]+).(?P<s4>[0-9]+)/$',views.result,name="result"),
    path('<ip_address>/',views.result,name="result"),
]
