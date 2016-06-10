"""v1dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from lapp.views import register,home,culture,center,east,general,history,login,north,south# 別忘了這裡也要改
admin.autodiscover()
# 每個連結都要在這宣告成像register一樣的格式
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^register/$', register),
    url(r'^$','lapp.views.home', name='home'),
    url(r'^culture/$', culture),
    url(r'^center/$',center),
    url(r'^east/$',east),
    url(r'^general/$',general),
    url(r'^history/$',history),
    url(r'^login/$',login),
    url(r'^north/$',north),
    url(r'^south/$',south),
]

