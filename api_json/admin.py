from django.contrib import admin
from api_json.models import SalasUF
from api_json.models import Filme
# Register your models here.
class Filmes(admin.ModelAdmin):
    list_display = ('titulo', 'genero')

class SalasUFs(admin.ModelAdmin):
    list_display = ('uf','qtd_salas', 'ano_atualizacao')

admin.site.register(Filme, Filmes)
admin.site.register(SalasUF, SalasUFs)