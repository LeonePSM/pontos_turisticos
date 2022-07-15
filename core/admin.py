from django.contrib import admin
from .models import PontoTuristico
from .actions import reprova_ponto,aprova_ponto

class PontoAdmin(admin.ModelAdmin):
    list_display = ['aprovado']
    actions = [reprova_ponto, aprova_ponto]

admin.site.register(PontoTuristico, PontoAdmin)