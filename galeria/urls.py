from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),  # Pagina principal do app, mostra as imagens
    path('imagem/', imagem, name='imagem'),
]