from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('mynet/',views.mynet,name='mynet'),
    path('login/',views.login,name='login'),
    path('resume/',views.resume,name='resume'),
    path('register/',views.register,name='register'),
    path('jobs/',views.jobs,name='jobs'),
    path('message/',views.message,name='message'),
    path('new/',views.notify,name='new'),
]