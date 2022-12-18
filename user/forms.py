from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'demo@gmail.com'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'User1234'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))

    class meta:
        model = User
        fields = ("email","username","password1","password2")
    
    def save(self, commit=True):
        user = super(UserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user