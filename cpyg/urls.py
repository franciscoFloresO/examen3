from django.contrib import admin
from django.urls import path 
from .views import index, feriados, formContacto, formReg, fotos, productos, qsomos, form_mod_cliente, form_mod_producto, form_crear_cliente, form_crear_producto, mostrar, mostrar2,  form_del_cliente, form_del_producto, botonera
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ 
    path ('', index, name="index"),
    path ('feriados/', feriados, name="feriados"),
    path ('formContacto/', formContacto, name="formContacto"),
    path ('formReg/', formReg, name="formReg"),
    path ('fotos/', fotos, name="fotos"),
    path ('productos/', productos, name="productos"),
    path ('qsomos/', qsomos, name="qsomos"),
    path ('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path ('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),
    path ('form_crear_cliente/', form_crear_cliente, name="form_crear_cliente"),
    path ('form_crear_producto/', form_crear_producto, name="form_crear_producto"), 
    path ('mostrar/', mostrar, name="mostrar"),
    path ('mostrar2/', mostrar2, name="mostrar2"),
    path ('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
    path ('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path ('botonera/', botonera, name="botonera"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)