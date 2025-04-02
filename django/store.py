from django.shortcuts import render


def store(request):
    '''
    Method creates a view for the online store page.

    :param object request: User inputs data into the system.

    :returns: Am html page to the online store.

    :return type: html

    '''
    return render(request, 'webapp/store.html')