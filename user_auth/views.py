from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'first.html')


def ouut(request):
    return render(request, 'logger_out.html')


def auth(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'singup.html', {'form': form})


def profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'account.html', {'username': username})