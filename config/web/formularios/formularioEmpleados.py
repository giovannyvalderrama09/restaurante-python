from django import forms



class FormularioEmpleados(forms.Form):

    Empleados=(
        (1,'Chefts'),
        (2,'Administrador'),
        (3,'Mesero'),
        (4,'Asistente de cheft')
    )

    nombreEmpleado=forms.CharField(
        label='Nombres Empleado:',
        required= True,
        max_length= 30,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )
    
    apellidosEmpleado=forms.CharField(
        label="Apellidos Empleado:",
        required= True,
        max_length= 30,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )

    tipo=forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control m-4'}),
        choices= Empleados
    )

    contactoEmergencia=forms.CharField(
        label="Numero de Contacto:",
        required= True,
        max_length= 30,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )
    foto=forms.CharField(
        required= True,
        max_length= 600,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )
