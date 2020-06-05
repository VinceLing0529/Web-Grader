from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('studentlogin/',views.studentlogin,name='studentlogin'),
    path('teacherlogin/',views.studentlogin,name='teacherlogin'),

    path('signup/',views.signup,name='signup')
]
