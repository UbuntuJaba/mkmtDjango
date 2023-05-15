from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('faculty/', faculty, name = 'faculty'),
    path('education/', education, name = 'education'),
    path('contacts/', contacts, name = 'contacts'),
    path('test/', test, name = 'test'),
]