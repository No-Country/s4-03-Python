from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='Alias', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))
    first_name = forms.CharField(label='Nombre(s)', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'first_name',
                                    'placeholder' : 'Nombre(s)'
                                }))
    last_name = forms.CharField(label='Apellidos', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'last_name',
                                    'placeholder' : 'Apellidos'
                                }))
    
    email = forms.EmailField(label='Correo electrónico', required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : 'form-control',
                                'id' : 'username',
                                'placeholder' : 'example@gmail.com'
        }))
    
    password = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control'
                                }))
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name
      
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')  

        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def clean_role(self):
        role = self.cleaned_data.get('email')
        return role
    
    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            password = self.cleaned_data.get('password'),
            email = self.cleaned_data.get('email'),
            
        )