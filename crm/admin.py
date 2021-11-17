from django.contrib import admin

from .models import CRMUser, Boardgames
from django.contrib.auth.models import User


class UserList(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name')
    list_filter = ('username', 'last_name')
    search_fields = ('username',)
    ordering = ['username']


class BoardgamesList(admin.ModelAdmin):
    list_display = ( 'boardgames_title', 'boardgames_BGG_rank')
 #   list_filter = ( 'boardgames_title')
    search_fields = ('boardgames_title',)
    ordering = ['boardgames_title']

admin.site.register(Boardgames, BoardgamesList)
