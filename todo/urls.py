from django.urls import path
from . import views

urlpatterns=[
    #path("",views.home,name="login"),
    path("",views.tasks,name="tasks"),
    #path("logOut",views.logoutView,name="logOut"),
    path("delete/<int:pk>",views.deleteView,name="deleteView"),
    path("update",views.editView,name="update"),
]