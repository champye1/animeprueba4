from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from .models import Perfil

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    grupo = forms.ModelChoiceField(
        queryset=Group.objects.filter(name='Editorlol'),
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Seleccione el grupo'
        }),
        label='Grupo de Usuario',
        initial=None
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'grupo']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Permitir acceso al admin
        if commit:
            user.save()
            grupo = self.cleaned_data.get('grupo')
            if grupo:
                grupo.user_set.add(user)  # Asignar el usuario al grupo
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class PerfilUpdateForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'max': timezone.now().date().isoformat()}),
        required=False
    )
    
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False,
        label='Avatar'
    )
    
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_nacimiento']
        
    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha and fecha > timezone.now().date():
            raise forms.ValidationError('La fecha de nacimiento no puede ser una fecha futura')
        return fecha 