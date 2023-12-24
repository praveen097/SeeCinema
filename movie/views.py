from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return HttpResponse("Hello, I am watching a movie")

@login_required
def home_page(request):
    return render(request, 'index.html')