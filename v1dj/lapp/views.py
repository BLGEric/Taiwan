# -*- coding: UTF-8 -*-

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
def center(request):
	return render_to_response('center.html',RequestContext(request,locals()))
def east(request):
	return render_to_response('east.html',RequestContext(request,locals()))
def general(request):
	return render_to_response('general.html',RequestContext(request,locals()))
def history(request):
	return render_to_response('history.html',RequestContext(request,locals()))
def login(request):
	return render_to_response('login.html',RequestContext(request,locals()))
def north(request):
	return render_to_response('north.html',RequestContext(request,locals()))
def register(request):
	return render_to_response('register.html',RequestContext(request,locals()))
def south(request):
	return render_to_response('south.html',RequestContext(request,locals()))

def newinfo(request):
	newinfo = Newinfo.objects.all()
	return render_to_response('newinfo.html',RequestContext(request,locals()))


