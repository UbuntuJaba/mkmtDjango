from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *

# Create your views here.
def index(request):
    return render(request, 'mkmt/index.html')

def faculty(request):
    return render(request, 'mkmt/faculty.html')

def education(request):
    program420301 = studyingPrograms.objects.get(id = '1')
    program420302 = studyingPrograms.objects.get(id = '2')
    program090303 = studyingPrograms.objects.get(id = '3')
    program530301 = studyingPrograms.objects.get(id = '4')
    program530302 = studyingPrograms.objects.get(id = '5')
    program530303 = studyingPrograms.objects.get(id = '6')
    program090402 = studyingPrograms.objects.get(id = '7')
    program090402S = studyingPrograms.objects.get(id = '8')
    program420405 = studyingPrograms.objects.get(id = '9')
    program420405S = studyingPrograms.objects.get(id = '10')
    program420405T = studyingPrograms.objects.get(id = '11')
    program420401 = studyingPrograms.objects.get(id = '12')
    program420401S = studyingPrograms.objects.get(id = '13')
    program420401T = studyingPrograms.objects.get(id = '14')
    program510403 = studyingPrograms.objects.get(id = '15')
    program530402 = studyingPrograms.objects.get(id = '16')
    return render(request, 'mkmt/education.html', {'program420301': program420301,
                                                   'program420302': program420302,
                                                   'program090303': program090303,
                                                   'program530301': program530301,
                                                   'program530302': program530302,
                                                   'program530303': program530303,
                                                   'program090402': program090402,
                                                   'program090402S': program090402S,
                                                   'program420405': program420405,
                                                   'program420405S': program420405S,
                                                   'program420405T': program420405T,
                                                   'program420401': program420401,
                                                   'program420401S': program420401S,
                                                   'program420401T': program420401T,
                                                   'program510403': program510403,
                                                   'program530402': program530402})


def test(request):
    # programs = studyingPrograms.objects.all()
    program420305 = studyingPrograms.objects.get(id = '2')
    return render(request, 'mkmt/test.html', {'program420305': program420305})

def contacts(request):
    return render(request, 'mkmt/contacts.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')