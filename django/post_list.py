from django.views.generic import ListView,

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