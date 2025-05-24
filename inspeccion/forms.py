from django import forms
from .models import OrdenInspeccion

class CierreOrdenInspeccionForm(forms.ModelForm):
    class Meta:
        model = OrdenInspeccion
        fields = ['fecha_cierre', 'observaciones']
        widgets = {
            'fecha_cierre': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
