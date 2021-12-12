from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.db.models import Sum
from _decimal import Decimal
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from .forms import PasswordResetReCaptchaForm

now = timezone.now()


def home(request):
    return render(request, 'crm/home.html',
                  {'crm': home})


@login_required
def user_list(request):
    user = User.objects.filter(is_active=True)
    return render(request, 'crm/user_list.html',
                  {'users': user})


@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # update
        user_form = UserForm(request.POST, instance=request.user)
        crmuser_form = CRMUserForm(request.POST, instance=request.user.crmuser)
        if user_form.is_valid() and crmuser_form.is_valid():
            user_form.save()
            crmuser_form.save()
            return render(request, 'crm/user_list.html')
    else:
        # edit
        user_form = UserForm(instance=request.user)
        crmuser_form = CRMUserForm(request.POST, instance=request.user.crmuser)
    return render(request, 'crm/user_edit.html', {
        'user_form': user_form,
        'crmuser_form': crmuser_form
    })


@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('crm:user_list')

@login_required
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    users = User.objects.filter(username=user.username)


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
    boardgames = get_object_or_404(Boardgames, pk=pk)
    boardgames = Boardgames.objects.filter(boardgames_title=boardgames.boardgames_title)

    return render(request, 'crm/boardgames_detail.html', {'boardgames': boardgames})

@login_required
def all_user_trade_list(request, pk):
    boardgames = get_object_or_404(Boardgames, pk=pk)
    #boardgames = Boardgames.objects.filter(boardgames_title=boardgames.boardgames_title)

    #user = get_object_or_404(BoardgamesAvailable)
    users = BoardgamesAvailable.objects.filter(boardgames=boardgames.id)

    return render(request, 'crm/all_user_trade_list.html', {'users': users})

#@login_required
#def all_user_want_list(request, pk):
#    boardgames = get_object_or_404(Boardgames, pk=pk)
#    boardgames = Boardgames.objects.filter(boardgames_title=boardgames.boardgames_title)

#    return render(request, 'crm/all_user_want_list.html', {'boardgames': boardgames})

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('crm:register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'crm/register.html', {'form': f})

class PasswordResetReCaptcha(PasswordResetView):
    form_class = PasswordResetReCaptchaForm

