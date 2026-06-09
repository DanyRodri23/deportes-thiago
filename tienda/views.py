from django.shortcuts import render, get_object_or_404
from .models import Producto


def inicio(request):
    productos = Producto.objects.filter(activo=True)

    return render(request, 'index.html', {
        'productos': productos
    })


def detalle_producto(request, producto_id):

    producto = get_object_or_404(
        Producto,
        id=producto_id
    )

    return render(
        request,
        'detalle_producto.html',
        {
            'producto': producto
        }
    )