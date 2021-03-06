from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.homepage,name='homepage'),
    url(r'^createuser/',views.createuser,name='createuser'),
    url(r'^login/',views.login_user,name='login'),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^savesurvey/',views.savesurvey,name='savesurvey'),
    url(r'^surveyresults/',views.surveyresults,name='surveyresults'),
    url(r'^about/',views.about,name='about'),
    url(r'^contactus/',views.contactus,name='contactus'),
    url(r'^exportcsv/',views.exportcsv,name='exportcsv'),
]
