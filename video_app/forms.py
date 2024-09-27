from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    first_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder':'First name',"id":"firstname"}))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'placeholder':'Last name'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':"Create password"}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'placeholder':"Confirm password"}))
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password1','password2')

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user
