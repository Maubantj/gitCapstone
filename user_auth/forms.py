from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    '''
    Create a form class which inherits from UserCreationForm provided
    within the Django Framework.
    :param: form UserCreationForm: Django's user creation form.
    '''
    # Activate email field, which exists in django framework.
    email = forms.EmailField()

    class Meta:
        '''
        Method updates the User model.
        '''
        # Specify model to interact with from parent class.
        model = User
        # List all fields.
        fields = ['username', 'email', 'password1', 'password2']
