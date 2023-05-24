from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.
def index(request):
    return render(request, 'mkmt/index.html')

def faculty(request):
    return render(request, 'mkmt/faculty.html')

def education(request):
    undergraduate = studyingPrograms.objects.all()
    magistr090402 = magistracy.objects.filter(title = '09.04.02 Информационные системы и технологии')
    magistr420405 = magistracy.objects.filter(title = '42.04.05 Медиакоммуникации')
    magistr420401 = magistracy.objects.filter(title = '42.04.01 Реклама и связи с общественностью')
    magistr510403 = magistracy.objects.filter(title = '51.04.03 Социально-культурная деятельность')
    magistr530402 = magistracy.objects.filter(title = '53.04.02 Вокальное искусство')
    return render(request, 'mkmt/education.html', {'undergraduate': undergraduate, 
                                              'magistr090402': magistr090402,
                                              'magistr420405': magistr420405,
                                              'magistr420401': magistr420401,
                                              'magistr510403': magistr510403,
                                              'magistr530402': magistr530402})


def test(request):
    # programs = studyingPrograms.objects.all()
    undergraduate = studyingPrograms.objects.all()
    magistr090402 = magistracy.objects.filter(title = '09.04.02 Информационные системы и технологии')
    magistr420405 = magistracy.objects.filter(title = '42.04.05 Медиакоммуникации')
    magistr420401 = magistracy.objects.filter(title = '42.04.01 Реклама и связи с общественностью')
    magistr510403 = magistracy.objects.filter(title = '51.04.03 Социально-культурная деятельность')
    magistr530402 = magistracy.objects.filter(title = '53.04.02 Вокальное искусство')
    return render(request, 'mkmt/test.html', {'undergraduate': undergraduate, 
                                              'magistr090402': magistr090402,
                                              'magistr420405': magistr420405,
                                              'magistr420401': magistr420401,
                                              'magistr510403': magistr510403,
                                              'magistr530402': magistr530402})

def contacts(request):
    return render(request, 'mkmt/contacts.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')