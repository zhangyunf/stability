from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("好久不见")
    return render(request, "index.html")
