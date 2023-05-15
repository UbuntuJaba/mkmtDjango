from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.
def index(request):
    return render(request, 'mkmt/index.html')

def faculty(request):
    return render(request, 'mkmt/faculty.html')

def education(request):
    return render(request, 'mkmt/education.html')

def test(request):
    programs = studyingPrograms.objects.all()
    return render(request, 'mkmt/test.html', {'programs': programs})

def contacts(request):
    return render(request, 'mkmt/contacts.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')