from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    '''Classe correspondente ao model Car que permite
    o gerenciamento, na visão de admin, da tabela carros.'''
    # As variaveis abaixo são baseadas na classe mãe
    # campos que devem aparecer no gerenciamento da aplicação:
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value',)
    # será possivel fazer busca baseado nesses campos de busca:
    search_fields = ('model',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)