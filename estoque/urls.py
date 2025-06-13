from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/<int:produto_id>/movimentar/', views.movimentar_estoque, name='movimentar_estoque'),
    path('categorias/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
] 