"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import test_view, test_extends_parent, test_extends_child, test_get, test_post, register, login_method, book_view, publication_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', test_view),
    url(r'^parent/', test_extends_parent),
    url(r'^child/', test_extends_child),
    url(r'^test_get/', test_get),
    url(r'^test_post/', test_post),
    url(r'^register/', register),
    url(r'^login/', login_method),
    url(r'^book/', book_view),
    url(r'^publication/', publication_view),
	

]
