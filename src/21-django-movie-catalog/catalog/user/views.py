from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password  = request.POST['password']

        user = auth.authenticate(username= username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,'Logged in successfully.')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Wrong username or password')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

# This view taught me how to use the messages framework to give the user
# feedback after a redirect instead of just rendering an error in place.
def register(request):
    if request.method == 'POST':

        # get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            # Username
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'This username is already taken.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'This email is already taken.')
                    return redirect('register')
                else:
                    # everything checks out
                    user = User.objects.create_user(username=username, password= password,email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Your account has been created.')
                    return redirect('login')
        else:
            print('passwords do not match')
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'You have been logged out.')
        return redirect('index')
