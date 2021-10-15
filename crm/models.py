from django.db import models

from django.utils import timezone
from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_name)


class Boardgames(models.Model):
    # user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boardgames')
    boardgames_title = models.CharField(max_length=100)
    boardgames_genre = models.CharField(max_length=50)
    boardgames_BGG_rank = models.IntegerField()
    boardgames_year = models.IntegerField(default='2021')
    boardgames_player_count_min = models.IntegerField()
    boardgames_player_count_max = models.IntegerField()
    boardgames_msrp = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.id)


class BoardgamesAvailable(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gamesAvailable')
    boardgames_title = models.CharField(max_length=100)
    boardgames_condition = models.TextField(max_length=50)
    boardgames_notes = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_name)


class BoardgamesRequested(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='GamesRequested')
    boardgames_title = models.CharField(max_length=100)
    boardgames_condition = models.TextField(max_length=50)
    boardgames_notes = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user_name)
