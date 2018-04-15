from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    loginform = AuthenticationForm()
    return(render(request,'website/index.html', {'loginform':loginform}))
    
def createuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('website:homepage')
    else:
        form = UserCreationForm()
        loginform=AuthenticationForm()
            
    return render(request,'website/createuser.html',{'form':form, 'loginform':loginform})

def login_user(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
    return redirect('website:homepage')
    
def logout_user(request):
    logout(request)
    return redirect('website:homepage')