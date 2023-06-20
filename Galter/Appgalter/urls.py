from django.urls import path
from Appgalter.views import listarUsuarios, InsertarUsuario
from . import views



urlpatterns = [
    path('Usuario', listarUsuarios.as_view(), name='Usuario'),
    path('insertarUsu/', InsertarUsuario.as_view(), name='insertarUsu'),

    #insertar datos con js
    path('frmInsertar',views.formularioInsertar, name='resgistrar')
    
    
]
