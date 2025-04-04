from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    '''
    Method registers a new user account on the database.
    :param object request: User inputs data into the system.
    :returns: A message to the user confirming account creation.
    :return type: text.
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome {username}! "
                                f"Your account has been created. You may login!")
            return redirect('login')
    else:
        form = UserRegisterForm()
        context = {'form': form} 
    return render(request, 'user_auth/register.html', context)


# user decorator to require login from user, after login user redirected
# to profile page.
@login_required
def profile(request):
    '''
    Method requires user to login.
    :param object request: User inputs data into the system.
    :returns: login page.
    :return type:   object.
    '''
    return render(request, 'user_auth/profile.html')
