"""project_phone_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from phone_book_app.views import AddPerson, ModifyPerson, DeletePerson, ShowPerson, \
    AddAddress, AllPerson, AddPhone, AddEmail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/$', AddPerson.as_view()),
    url(r'^modify/(?P<id>(\d)+)/$', ModifyPerson.as_view()),
    url(r'^delete/(?P<id>(\d)+)/$', DeletePerson.as_view()),
    url(r'^show/(?P<id>(\d)+)/$', ShowPerson.as_view()),
    url(r'^modify/(?P<id>(\d)+)/addAddress/$', AddAddress.as_view()),
    url(r'^adres/$', AllPerson.as_view()),
    url(r'^modify/(?P<id>(\d)+)/addPhone/$', AddPhone.as_view()),
    url(r'^modify/(?P<id>(\d)+)/addEmail/$', AddEmail.as_view())
]
