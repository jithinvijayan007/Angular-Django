from django.contrib import admin
from django.conf.urls import url
from testapp import views
from testapp.views import UserList

urlpatterns = [
    url(r'^register/',views.register,name="register"),
    url(r'^user/',views.userform,name="userform"),
    url(r'^list/',views.userlist, name="list"),

]
