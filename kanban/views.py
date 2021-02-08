from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("仮のトップページです")
    return render(request, "kanban/index.html")

@login_required
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect('kanban:home')
    else:
        form = UserCreationForm()

    context = {
        "form":form
    }
    return render(request, 'kanban/signup.html', context)