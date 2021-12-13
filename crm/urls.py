from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .forms import PasswordResetReCaptchaForm

app_name = 'crm'
urlpatterns = [
    #url(r'^register/$', views.register, name='register'),
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user_list', views.user_list, name='user_list'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/detail/', views.user_detail, name='user_detail'),
    path('boardgames_list', views.boardgames_list, name='boardgames_list'),
    path('boardgames/create/', views.boardgames_new, name='boardgames_new'),
    path('boardgames/<int:pk>/edit/', views.boardgames_edit, name='boardgames_edit'),
    path('boardgames/<int:pk>/delete/', views.boardgames_delete, name='boardgames_delete'),
    path('boardgames/<int:pk>/detail/', views.boardgames_detail, name='boardgames_detail'),
    path('password_reset/', views.PasswordResetReCaptcha.as_view(), name='password_reset'),
    path('user/<int:pk>/trade/', views.all_user_trade_list, name='all_user_trade_list'),
    path('user/<int:pk>/want/', views.all_user_want_list, name='all_user_want_list'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
