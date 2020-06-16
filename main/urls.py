from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name="index"),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('teacherlogin/',views.teacherlogin,name='teacherlogin'),
    path('signup/',views.signup,name='signup')
]
