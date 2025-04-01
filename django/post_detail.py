from django.views.generic import DetailView
from .models import Post


class PostDetailView(DetailView):
    '''
    Create PostDetailView class which inherits from django's DetailView.
    No modification to Django's standard view.
    :param function DetailView: Django's DetailView.
    :returns: A post.
    :return type: object.
    '''
    model = Post