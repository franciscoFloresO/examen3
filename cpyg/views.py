from django.shortcuts import redirect, render
from django.views.decorators import csrf
from .models import Producto, Cliente
from .forms import ProductoForm, ClienteForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def feriados(request):
    return render(request, 'feriados.html')
    
def formContacto(request):
    return render(request,'formContacto.html')

def formReg(request):
    return render(request,'formReg.html')

def fotos(request):
    return render(request,'fotos.html')

def productos(request):
    return render(request,'productos.html')

def qsomos(request):
    return render(request,'qsomos.html')

def form_crear_cliente(request):
    return render(request, 'form_crear_cliente.html')

def form_crear_producto(request):
    return render(request, 'form_crear_producto.html')

def form_mod_cliente(request):
    return render(request, 'form_mod_cliente.html')

def form_mod_producto(request):
    return render(request, 'form_mod_producto.html')

def botonera(request):
    return render(request, 'botonera.html')

def mostrar2(request):
    producto = Producto.objects.all()
    datos={
        'producto' : producto
        }
    return render(request, 'mostrar2.html', datos)

def mostrar(request):
    cliente = Cliente.objects.all()
    datos={
        'cliente' : cliente
    }
    return render(request, 'mostrar.html', datos)

def form_producto(request):
    if request.method=='POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('mostrar2')
    else:
        producto_form = ProductoForm()
        return render(request, 'form_crear_producto.html',{'producto_form': producto_form})

def form_modproducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    datos={
        'form': ProductoForm(instance = producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar2')

    return render(request, 'form_mod_producto.html', datos)

def form_del_producto(request,id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect('mostrar2')

def form_crear_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('mostrar')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})


def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar')
    return render(request, 'form_mod_cliente.html', datos)


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('mostrar')
