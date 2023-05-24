from django.contrib import admin
from .models import *
# Register your models here.

class magistracyAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile')
    list_display_links = ('id', 'profile')


admin.site.register(studyingPrograms)
admin.site.register(magistracy, magistracyAdmin)