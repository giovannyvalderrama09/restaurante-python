from django import forms


class FormularioPlatos(forms.Form):

    PLATOS=(
        (1,'Entrada'),
        (2,'Plato fuerte'),
        (3,'Postre'),
    )

    nombre=forms.CharField(
        required= True,
        max_length= 30,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )
    descripcion=forms.CharField(
        required=False,
        max_length=250,
        widget= forms.Textarea(attrs={'class': 'form-control   m-4'})

    )
    fotografia=forms.CharField(
        required= True,
        widget= forms.TextInput(attrs={'class': 'form-control m-4'})
    )
    precio=forms.CharField(
        required= True,
        max_length=20,
        widget= forms.NumberInput(attrs={'class': 'form-control m-4'})
    )
    especialidad=forms.ChoiceField(
        required= True,
        widget= forms.Select(attrs={'class': 'form-control m-4'}),
        choices= PLATOS
    )

