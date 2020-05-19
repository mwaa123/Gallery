from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('',views.welcome,name='welcome'),
     url(r'^people/',views.people,name = 'people')
]
