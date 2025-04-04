from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    '''
    Create a class called Post for the blog posts from scratch.
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        This method returns a string representation of the Post object.
        The admin page will be able to display the title of each post.
        :param: none.
        :returns: string representation of the object.
        :return type: string.
        '''
        return self.title

    def get_absolute_url(self):
        '''
        This method returns the post detail after user updates a post.
        :param: none.
        :returns: detailed post.
        :return type: object.
        '''
        return reverse('post-detail', kwargs={'pk': self.pk})
