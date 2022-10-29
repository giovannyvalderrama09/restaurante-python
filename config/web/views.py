from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos


# Create your views here.

#Todas las vistas son funciones de python

def Home(request):
    return render(request, 'home.html')


# def Platos(request):
#     return render(request, 'menuPlatos.html')    


def Empleados(request):
    return render(request, 'empleados.html')  


def Platos(request):

    formulario=FormularioPlatos()

    data={
    'formulario':formulario
}    

    return render(request, 'menuPlatos.html',data)


