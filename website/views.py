from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def homepage(request):
    return(render(request,'website/index.html'))
    
def createuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('website:homepage')
    else:
        form = UserCreationForm()
            
    return render(request,'website/createuser.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return render(request, 'website:homepage')
        else:
            form=AuthenticationForm()
            
    return render(request,'website:login')