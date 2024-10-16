from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria  # Especifica el modelo aquí
        fields = ['descripcion', 'estado']  # Asegúrate de que los nombres de los campos son correctos
        labels = {
            'descripcion': "Descripción de la categoría",
            'estado': "Estado"
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'})  # Asumiendo que 'estado' es un campo de selección
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not field.widget.attrs.get('class'):
                field.widget.attrs.update({'class': 'form-control'})