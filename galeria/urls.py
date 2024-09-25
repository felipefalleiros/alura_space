from django.urls import path
from galeria.views import index, imagem

# Isola as urls relacionadas a galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]