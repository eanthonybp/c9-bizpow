from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import authenticate, login, logout
from .forms import SurveyForm
from .models import Survey
import StringIO
from django.http import HttpResponse
import csv


# Create your views here.
def homepage(request):
    loginform = AuthenticationForm()
    surveyform = SurveyForm() 
    return(render(request,'website/index.html', {'loginform':loginform, 'surveyform':surveyform}))
    
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
    
def savesurvey(request):
    if request.POST:
        form = SurveyForm(request.POST)
        if form.is_valid:
            form.save()
    
    return redirect('website:homepage')

@permission_required('is_superuser')   
def surveyresults(request):
    surveys = Survey.objects.all().order_by('submitted')
    return render(request,'website/survey_list.html',{'surveys':surveys})
    
def about(request):
    return render(request,'website/about.html')
    
def contactus(request):
    return render(request,'website/contactus.html')

@permission_required('is_superuser')
def exportcsv(request):
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Email",
        "Biggest Problem",
        "Submitted",
        ])
    surveys = Survey.objects.all()
    for obj in surveys:
        writer.writerow([
            obj.email_contact,
            obj.biggest_problem,
            obj.submitted,
        ])
        print(obj.email_contact + 
            obj.biggest_problem
            )

    return response