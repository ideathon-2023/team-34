#Forms are basically used for taking input from the user in some manner and 
#using that information for logical operations on database

from django.forms import ModelForm

from django.contrib.auth.models import User 

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']