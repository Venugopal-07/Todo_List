from django.urls import path
from . import views

urlpatterns=[
    path("",views.tasks,name="tasks"),
    path("delete/<int:pk>",views.deleteView,name="deleteView"),
    path("update",views.editView,name="update"),
]