from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados



# Create your views here.

#Todas las vistas son funciones de python

def Home(request):
    return render(request, 'home.html')


# def Platos(request):
#     return render(request, 'menuPlatos.html')    


def Empleados(request):

    formularioEmpleados=FormularioEmpleados()
    data={
        'formularioEmpleados':formularioEmpleados
    }
    return render(request, 'empleados.html',data)  


def Platos(request):

    formulario=FormularioPlatos()

    data={
    'formulario':formulario
}    

    return render(request, 'menuPlatos.html',data)


