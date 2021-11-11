from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('user_list', views.user_list, name='user_list'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/delete/', views.user_detail, name='user_detail'),
    path('boardgames_list', views.boardgames_list, name='boardgames_list'),
    path('boardgames/create/', views.boardgames_new, name='boardgames_new'),
    path('boardgames/<int:pk>/edit/', views.boardgames_edit, name='boardgames_edit'),
    path('boardgames/<int:pk>/delete/', views.boardgames_delete, name='boardgames_delete'),
    path('boardgames/<int:pk>/detail/', views.boardgame_detail, name='boardgame_detail'),
    path('accounts/login/register/', views.register, name='register'),
]
