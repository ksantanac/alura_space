from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    # Forma de mostrar os campos do django admin
    list_display = ("id", "nome", "legenda", "publicada")
    
    # Campos que possa clicar para editar
    list_display_links = ( "id", "nome")
    
    # Adiciona um campo de buscar que procurará por nome
    search_fields = ("nome",)
    
    # Criar um filtro por categoria
    list_filter = ('categoria',)
    
    # Campo editável na lista
    list_editable = ("publicada", )
    
    # Quantidade de itens para quebrar página
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
