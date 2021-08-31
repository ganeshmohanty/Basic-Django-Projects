from django.urls import path
from . import views
urlpatterns=[
    path('',views.apioverview,name='api-overview'),
    path('task-list/',views.tasklist,name='task-list'),
    path('task-detail/<int:pk>/',views.taskdetail,name='task-detail'),
    path('task-create/',views.taskcreate,name='task-create'),
    path('task-update/<int:pk>/',views.taskupdate,name='task-update'),
    path('task-delete/<int:pk>/',views.taskdelete,name='task-delete'),



]