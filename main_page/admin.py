from django.contrib import admin
from .models import Ciekawostki

# Register your models here.


@admin.register(Ciekawostki)
class CiekawostkiAdmin(admin.ModelAdmin):
    list_display = ('liczbaporzadkowa', 'ciekawostka')
    fields = ['liczbaporzadkowa', 'ciekawostka']
