from django.urls import path
from rest_cliente.views import lista_cliente

urlpatterns= [
    path('lista_cliente', lista_cliente, name= "lista_cliente"),
]