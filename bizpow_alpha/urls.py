from django.conf.urls import url, include
from django.contrib import admin
from website import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/',include('website.urls')),
    url(r'^$',include('website.urls')),
]
