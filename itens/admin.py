from django.contrib import admin
from .models import Tipo, Itens

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Itens)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'descricao')
    search_fields = ('nome', 'tipo__nome')
    list_filter = ('tipo',)

