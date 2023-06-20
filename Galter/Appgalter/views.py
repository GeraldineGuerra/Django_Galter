import json
from typing import Any
from django.http import JsonResponse
from django.shortcuts import render


from Appgalter.models import usuario
from Appgalter.models import proveedor
from Appgalter.models import cliente, material, pedido, producto

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import ListView,View





def principal (request):
    listarUsuarios=usuario.objects.all()
    return render(request,"index1.html",{'usu': listarUsuarios})



# class listarUsuarios(ListView):
#     model=usuario
#     template_name="index1.html"

    


# class listarProveedor(ListView):
#     model=proveedor
#     template_name="index2.html"




# class listarCliente(ListView):
#     model=cliente
#     template_name="index3.html"



# class listarMaterial(ListView):
#     model=material
#     template_name="index4.html"




# class listarProducto(ListView):
#     model=producto
#     template_name="index5.html"



# class listarPedido(ListView):
#     model=pedido
#     template_name="index6.html"






# class listarUsuarios(View):
#     def get(self,request):
#         datos=usuario.objects.all().values()
#         datosusu=list(datos)
#         return render(request, 'index1.html',{'datos': datosusu})
        
#         #return JsonResponse(datosusu, safe=False)
    




class listarUsuarios(ListView):
    def get(self,request):
        datos=usuario.objects.all()
        datos_Usuarios=[]
        for i in datos:
            datos_Usuarios.append({ 
                'codi_usuario':i.codi_usuario,
                'nombre_usuario':i.nombre_usuario,
                'correo_usuario':i.correo_usuario,
                'pass_ususario':i.pass_ususario,
                'tipo_usuario':i.tipo_usuario
            }) 
        #datoscli=list(datos)
        return JsonResponse(datos_Usuarios, safe=False)
        #return render(request, 'index.html',{'datos': datoscli})
    








class InsertarUsuario(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        try:
            datos=json.loads(request.body)
        except(json.JSONDecodeError,UnicodeDecodeError):
            return JsonResponse({"error": "Erra en la decodificacion"})
        datos=json.loads(request.body)
        codi_usuario = datos.get('codi_usuario')
        nombre_usuario = datos.get('nombre_usuario')
        correo_usuario = datos.get('correo_usuario')
        pass_usuario = datos.get('pass_usuraio')
        tipo_usuario = datos.get('tipo_usuraio')
        print("datos del usuario", request.POST)
        #cli=Cliente.objects.create(codi_usuario=datos['codi_usuario'],nombre_usuario=datos['nombre_usuario'],correo_usuario=datos['correo_usuario'],pass_usuraio=datos['pass_usuraio'],tipo_usuraio=datos['tipo_usuraio'])
        #cli.save()
        #return JsonResponse({'mensaje': 'datos guardados'})
        usuario.objects.create(codi_usuario=codi_usuario, nombre_usuario=nombre_usuario, correo_usuario=correo_usuario, pass_usuario=pass_usuario, tipo_usuario=tipo_usuario)
        return JsonResponse({'mensaje': 'datos guardados'})
        # return render(request,'insertarCli.html',{'mensaje': 'Datos guardados'})






def formularioInsertar(request):
    return render(request,"insertarUsu.html")    






class Actualizar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def put(self,request,pk):
        try:
            registro=usuario.objects.get(pk=pk)

        except usuario.DoesNotExist:
            return JsonResponse({"Error": "El documento no existe"})
        
        data=json.loads(request.body)
        registro.nombre=data.get('nombre_usuario')
        registro.correo=data.get('correo_usuario')
        registro.password=data.get('pass_ususario')
        registro.tipo=data.get('tipo_usuario')
        registro.save()
        return JsonResponse({"mensaje": "datos  del usuario actualizados"})


