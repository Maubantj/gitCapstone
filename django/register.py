from django.shortcuts import render
from django.contrib import messages


def register(request):
    '''
    Method registers a new user account on the database.

    :param object request: User inputs data into the system.

    :returns: A message to the user confirming account creation.
    
    :return type: str.
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