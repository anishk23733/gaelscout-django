from django.shortcuts import render
from django.http import HttpResponse
from teamindex.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    return render(request, 'index.html')

def teamindex(request):
    teams = Teams.objects.all()
    paginator = Paginator(teams, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    teams = paginator.get_page(page)
    return render(request, 'teamindex.html', {'teams': teams})

def dashboard(request, team_number):
    return render(request, 'dashboard.html', {'team':team_number})