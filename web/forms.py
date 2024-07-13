#from django import forms

#class ContactFormForm(forms.Form):
#    customer_email = forms.EmailField(label='Correo')
#    customer_name = forms.CharField(max_length=64,label='Nombre')
#    message = forms.CharField(widget=forms.Textarea, label='Mensaje')

from django import forms
from .models import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

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
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        error_messages={
            'required': 'El correo electrónico es obligatorio',
            'invalid': 'Introduce una dirección de correo electrónico válida',
        }
    )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','last_name','password1', 'password2')
        labels =  {
            'username': 'Nombre de Usuario',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Repita Contraseña',
        }
        error_messages = {
            'username': {
                'required': 'El nombre de usuario es obligatorio',
                'unique': 'Este nombre de usuario ya está en uso',
            },
            'password1': {
                'required': 'La contraseña es obligatoria',
            },
            'password2': {
                'required': 'Repite la contraseña',
                'password_mismatch': 'Las contraseñas no coinciden',
            },
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Repita Contraseña'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellidos'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Este correo electrónico ya está en uso')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError('Las contraseñas no coinciden')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está en uso')
        return username