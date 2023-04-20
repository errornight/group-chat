from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_groups, name='AllGroups'),
    path('<uuid:uuid>/', views.group_detail, name='GroupDetail'),
    path('create/', views.create_room, name='CreateRoom')
]