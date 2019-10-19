from django.contrib import admin
from .models import Curiosity

# Register your models here.


@admin.register(Curiosity)
class CuriosityAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    fields = ['id', 'text']
