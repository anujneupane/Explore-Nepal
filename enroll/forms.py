from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    password1= forms.CharField(label='Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2= forms.CharField(label='Confirm Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email= forms.CharField(required=True,label='Email', widget = forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets ={'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs= {'autocomplete':'current-password' ,'class':'form-control'}))

class Changepassword(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),strip=False,widget =forms.PasswordInput(attrs={'autofocus':True,'class':'form-control','autocomplete':'current-password'}))
    new_password1 = forms.CharField( label=_('New Password'),strip=False,widget =forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),help_text = password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField( label=_('Confirm Password'),strip=False,widget =forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'new-password'})) 

class MyPasswordResetForm(PasswordResetForm):
   email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email",'class':'form-control'}),
    )   
   
class MySetPasswordForm(SetPasswordForm):
     new_password1 = forms.CharField( label=_('New Password'),strip=False,widget =forms.PasswordInput(attrs={'class':'form-control','autocomplete':'new-password'}),help_text = password_validation.password_validators_help_text_html())
     
     new_password2 = forms.CharField( label=_('Confirm Password'),strip=False,widget =forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'new-password'})) 

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','province','zipcode']
        widgets = {
                   'name':forms.TextInput(attrs={'class':'form-control'}),
                   'locality':forms.TextInput(attrs={'class':'form-control'}),
                   'city':forms.TextInput(attrs={'class':'form-control'}),
                   'province':forms.Select(attrs={'class':'form-control'}),
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                   } 


