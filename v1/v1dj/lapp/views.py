from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template import RequestContext
from lapp.models import Logindb
# 每個連結都要在這宣告成像home一樣的格式
def register(request):
	if request.POST:
		username = request.POST['tbusername']
		account = request.POST['tbaccount']
		password = request.POST['tbpassword']
		Logindb.objects.create(
			username = username,
			account = account,
			password = password
		)
	return render_to_response('register.html',RequestContext(request,locals()))
def home(request):
	return render_to_response('home.html',RequestContext(request,locals()))
def culture(request):
	return render_to_response('culture.html',RequestContext(request,locals()))

