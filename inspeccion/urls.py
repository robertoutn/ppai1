from django.urls import path
from . import views

urlpatterns = [
    path('orden/<int:pk>/cerrar/', views.cerrar_orden_inspeccion, name='cerrar_orden_inspeccion'),
    path('orden/<int:pk>/', views.detalle_orden_inspeccion, name='detalle_orden_inspeccion'),
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
]
