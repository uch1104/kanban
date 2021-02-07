from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

def index(request):
    # return HttpResponse("仮のトップページです")
    return render(request, "kanban/index.html")