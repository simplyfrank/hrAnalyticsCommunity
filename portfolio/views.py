from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('The Index page for "Portfolio"')