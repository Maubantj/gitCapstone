from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create classed below.


class PostListView(ListView):
    '''
    Create PostListView class which inherits from django's ListView.
    :param function ListView: Django's Listview.
    :returns: List of posts.
    :return type: objects.
    '''
    # State the model.
    model = Post
    # Override django template naming convention which is
    # <app>/<model>_<viewtype>.html (blog/post_list.html)
    template_name = 'blog/home.html'
    # Override context name to replace <model>_<viewtype> (post_list).
    context_object_name = 'posts'
    # order from posts from last to first.
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    '''
    Create PostDetailView class which inherits from django's DetailView.
    No modification to Django's standard view.
    :param function DetailView: Django's DetailView.
    :returns: A post.
    :return type: object.
    '''
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    Create PostCreateView class which inherits from django's CreateView.
    :param function LoginRequiredMixin CreateView: Django functions.
    :returns: a new post.
    '''
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        '''
        This method will populate the author name to the Post before
        form validation, since the data in the form is cleared post
        validation.
        :returns: an updated form.
        :return type: object
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    Create PostUpdateView class which inherits from django's UpdateView.
    :param function LoginRequiredMixin UserPassesTestMixin CreateView: Django functions.
    :returns: an updated post.
    :return type: object
    '''
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        '''
        This method will populate the author name to the Post before
        form validation, since the data in the form is cleared post
        validation.
        :param form object: user form.
        :returns: an updated form.
        :return type: object
        '''
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        '''
        This method tests if the user updating the post is the creator.
        :param: none
        :returns: Status code.
        :return type: Boolean.
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''
    Create PostDeleteView class which inherits from django's DeleteView.
    :param function LoginRequiredMixin UserPassesTestMixin DeleteView: Django functions.
    :returns: an updated post.
    :return type: object
    '''
    model = Post

    success_url = '/blog/'  # from project root.

    def test_func(self):
        '''
        This method tests if the user deleting the post is the creator.
        :param: none
        :returns: Status code 403 Forbidden
        :return type: Boolean.
        '''
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  # returns status code 403 forbidden.
