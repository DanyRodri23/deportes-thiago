from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.inicio,
        name='inicio'
    ),

    path(
        'producto/<int:producto_id>/',
        views.detalle_producto,
        name='detalle_producto'
    ),

]