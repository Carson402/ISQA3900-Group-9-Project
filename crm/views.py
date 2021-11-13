from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.db.models import Sum
from _decimal import Decimal

now = timezone.now()


def home(request):
    return render(request, 'crm/home.html',
                  {'crm': home})


@login_required
def user_list(request):
    user = User.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/user_list.html',
                  {'users': user})


@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # update
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.updated_date = timezone.now()
            user.save()
            user = User.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/user_list.html',
                          {'users': user})
    else:
        # edit
        form = UserForm(instance=user)
    return render(request, 'crm/user_edit.html', {'form': form})


@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('crm:user_list')

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    user = User.objects.filter(created_date__lte=timezone.now())
    users = user.objects.filter(user_name=pk)

    return render(request, 'crm/user_detail.html', {'users': users})

@login_required
def boardgames_list(request):
    boardgames = Boardgames.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/boardgames_list.html', {'boardgames': boardgames})

@login_required
def boardgames_new(request):
    if request.method == "POST":
        form = BoardGameForm(request.POST)
        if form.is_valid():
            boardgames = form.save(commit=False)
            boardgames.created_date = timezone.now()
            boardgames.save()
            boardgames = Boardgames.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/boardgames_list.html',
                          {'boardgames': boardgames})
    else:
        form = BoardGameForm()
        # print("Else")
    return render(request, 'crm/boardgames_new.html', {'form': form})

@login_required
def boardgames_edit(request, pk):
    boardgames = get_object_or_404(Boardgames, pk=pk)
    if request.method == "POST":
        form = BoardGameForm(request.POST, instance=boardgames)
        if form.is_valid():
            boardgames = form.save()
            # boardgames.user = boardgames.id
            boardgames.updated_date = timezone.now()
            boardgames.save()
            boardgames = Boardgames.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/boardgames_list.html', {'boardgames': boardgames})
    else:
        # print("else")
        form = BoardGameForm(instance=boardgames)
    return render(request, 'crm/boardgames_edit.html', {'form': form})


@login_required
def boardgames_delete(request, pk):
    boardgames = get_object_or_404(Boardgames, pk=pk)
    boardgames.delete()
    return redirect('crm:boardgames_list')

@login_required
def boardgames_detail(request, pk):
    boardgames = get_object_or_404(User, pk=pk)
    boardgames = Boardgames.objects.filter(created_date__lte=timezone.now())
    boardgames = Boardgames.objects.filter(boardgames_title=pk)

    return render(request, 'crm/boardgames_list.html', {'boardgames': boardgames})

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        user = get_object_or_404(User)
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.save()
            return render(request, 'crm/home.html',
                          {'user': user})
