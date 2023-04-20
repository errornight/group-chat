from django.urls import path
from . import views

urlpatterns = [
    path('', views.startup, name='Startup'), 
    path('login/', views.login_user, name='Login'), 
    path('logout/', views.logout_user, name='Logout'),
    path('profile/', views.profile, name='Profile'), 
    path('profile/edit/', views.edit_profile, name='EditProfile'),
    path('profile.change-password/', views.change_password, name='ChangePassword')
]
