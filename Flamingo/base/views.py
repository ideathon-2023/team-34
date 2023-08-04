from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def loginpage(request):
    page="login"
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,"User does not exists !")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Username or password does not exist")

    context = {'page': page}
    return render(request, 'base/login_register_old.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'An error has occured during registration')

    context ={'form': form}
    return render(request,'base/login_register_old.html', context)


#index = homepage
def index(request):
    return render(request,'base/index.html')

def hairtype(request):
    return render(request,'base/hairtype.html')

def skintype(request):
    return render(request,'base/skintype.html')

def natskin(request):
    return render(request,'base/natural_skin.html')

def nathair(request):
    return render(request,'base/natural_shair.html')

def artnat(request):
    return render(request,'base/artnat.html')

def about(request):
    return render(request,'base/about.html')

def contact(request):
    return render(request,'base/contact.html')

def logoutUser(request):
    logout(request)
    return redirect('index')