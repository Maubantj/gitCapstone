from django.shortcuts import render


# Create a view for the home page.
def home(request):
    '''
    Method creates a view for the home page.
    :param object request: http protocol.
    :returns: html web page.
    :return type: html
    '''
    return render(request, 'webapp/home.html')


# Create a view for the store.
def store(request):
    '''
    Method creates a view for the online store page.
    :param object request: http protocol.
    :returns: html web page.
    :return type: html
    '''
    return render(request, 'webapp/store.html')
