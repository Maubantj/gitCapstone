from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Create a class called profile. This will capture user information.
    The class inherits from Django's Model.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        This method returns a string representation of the Profile object.
        '''
        return f"{self.user.username} Profile"
