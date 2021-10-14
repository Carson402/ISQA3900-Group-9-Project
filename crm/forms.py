from django import forms
from .models import User, Boardgames

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'user_first_name', 'user_last_name', 'user_email', 'address', 'city',
                  'state', 'zipcode', 'phone_number')


class BoardGameForm(forms.ModelForm):
   class Meta:
       model = Boardgames
       fields = ( 'boardgames_title', 'boardgames_genre', 'boardgames_BGG_rank',
                 'boardgames_player_count_min', 'boardgames_player_count_max', 'boardgames_msrp')

