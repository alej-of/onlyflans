#from django import forms

#class ContactFormForm(forms.Form):
#    customer_email = forms.EmailField(label='Correo')
#    customer_name = forms.CharField(max_length=64,label='Nombre')
#    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        required = ['customer_email','customer_name','message']
        labels = {
            'customer_email': 'Correo',
            'customer_name': 'Nombre',
            'message': 'Mensaje'
        }
        widgets = {
            'customer_email': forms.EmailInput(attrs={'class':'form-control'}),
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 15, 'class':'form-control'},),
        }
        
        error_messages = {
            'customer_email': {
                'invalid': 'Ingrese un correo válido.',
                'required': 'Este campo es obligatorio.',
            },
            'customer_name': {
                'required': 'Este campo es obligatorio.',
            },
            'message': {
                'required': 'Este campo es obligatorio.',
            },
        }
