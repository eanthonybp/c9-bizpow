from django.conf.urls import url
from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.homepage,name='homepage'),
    url(r'^createuser/',views.createuser,name='createuser'),
    url(r'^login/',views.login_user,name='login'),
    url(r'^logout/',views.logout_user,name='logout'),
]
