from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos  
from web.models import Empleados



# Create your views here.

#Todas las vistas son funciones de python

def Home(request):
    return render(request, 'home.html')


# def Platos(request):
#     return render(request, 'menuPlatos.html')    


def EmpleadosVista(request):

    formularioEmpleados=FormularioEmpleados()
    data={
        'formularioEmpleados':formularioEmpleados
    }

    if request.method == 'POST':
        datosFormularioEmpleados = FormularioEmpleados(request.POST)
        if datosFormularioEmpleados.is_valid():
            datosLimpios=datosFormularioEmpleados.cleaned_data
            print(datosLimpios)

            empleadoNuevo = Empleados(
                nombre_empleados=datosLimpios["nombreEmpleado"],
                apellidos_empleados=datosLimpios["apellidosEmpleado"],
                tipo=datosLimpios["tipo"],
                numerocontacto=datosLimpios["contactoEmergencia"],
                foto=datosLimpios["foto"],
            )

            try:
                empleadoNuevo.save()
                print("Exito guardando datos")
            except Exception as error:
                    print("ups",error)

    
    return render(request, 'empleados.html',data)  


def PlatosVista(request):

    formulario=FormularioPlatos()

    data={
    'formulario':formulario
}    
# RECIBIMOS LOS DATOS DEL FORMULARIO

    if request.method == 'POST':
        datosFormularioPlatos = FormularioPlatos(request.POST)
        if datosFormularioPlatos.is_valid():
            datosLimpios=datosFormularioPlatos.cleaned_data
            print(datosLimpios)
            #construir diccionario de envio de datos hacia la db
            platoNuevo = Platos(
                nombreplato=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                especialidad=datosLimpios["especialidad"],
            )
            # Intentare enviar mis datos a la bd   
            try:
                platoNuevo.save()
                print("Exito guardando datos")
            except Exception as error:
                print("ups",error)                
    return render(request, 'menuPlatos.html',data)


