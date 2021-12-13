from django import forms
from .models import CRMUser, Boardgames
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CRMUserForm(forms.ModelForm):
    class Meta:
        model = CRMUser
        fields = ('address', 'city', 'state', 'zipcode', 'phone_number')


class BoardGameForm(forms.ModelForm):
    class Meta:
        model = Boardgames
        fields = ('boardgames_title', 'boardgames_genre', 'boardgames_BGG_rank', 'boardgames_year',
                  'boardgames_player_count_min', 'boardgames_player_count_max', 'boardgames_msrp')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class PasswordResetReCaptchaForm(PasswordResetForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
