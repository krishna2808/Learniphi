# from django.forms import ModelForm

from django import forms
from .models import User



 
class UserLogin(forms.Form):
    email  = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    # class Meta:
    #     model = User
    #     fields = ('email', 'password', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2  


    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2: 
            if password1 != password2:
                # raise forms.ValidationError('Password Not Matched')
                self.add_error('re_password', "passwords do not match !")


   
    
