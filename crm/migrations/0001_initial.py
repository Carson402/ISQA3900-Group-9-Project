# Generated by Django 3.2.7 on 2021-10-14 21:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boardgames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgames_title', models.CharField(max_length=100)),
                ('boardgames_genre', models.TextField(max_length=50)),
                ('boardgames_BGG_rank', models.IntegerField()),
                ('boardgames_player_count_min', models.IntegerField()),
                ('boardgames_player_count_max', models.IntegerField()),
                ('boardgames_msrp', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_first_name', models.CharField(max_length=50)),
                ('user_last_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoardgamesRequested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgames_title', models.CharField(max_length=100)),
                ('boardgames_condition', models.TextField(max_length=50)),
                ('boardgames_notes', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GamesRequested', to='crm.user')),
            ],
        ),
        migrations.CreateModel(
            name='BoardgamesAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boardgames_title', models.CharField(max_length=100)),
                ('boardgames_condition', models.TextField(max_length=50)),
                ('boardgames_notes', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gamesAvailable', to='crm.user')),
            ],
        ),
    ]
