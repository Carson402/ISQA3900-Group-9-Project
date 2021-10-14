from django.contrib import admin

from .models import User, Boardgames


class UserList(admin.ModelAdmin):
    list_display = ('user_name', 'user_last_name', 'user_first_name')
    list_filter = ('user_name', 'user_last_name')
    search_fields = ('user_name',)
    ordering = ['user_name']


class BoardgamesList(admin.ModelAdmin):
    list_display = ( 'boardgames_title', 'boardgames_BGG_rank')
 #   list_filter = ( 'boardgames_title')
    search_fields = ('boardgames_title',)
    ordering = ['boardgames_title']


admin.site.register(User, UserList)
admin.site.register(Boardgames, BoardgamesList)
