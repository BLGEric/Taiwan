# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import template
from django.template import RequestContext
from lapp.models import Logindb, Newinfo
from django.contrib import messages
# 每個連結都要在這宣告成像home一樣的格式
def register(request):
	login = request.session['login']
	if request.POST:
		username = request.POST['tbusername']
		account = request.POST['tbaccount']
		password = request.POST['tbpassword']
		confirm = request.POST['tbconfirm']
		if password == confirm:
			if Logindb.objects.filter(account=account).count()==0:
				Logindb.objects.create(
					username = username,
					account = account,
					password = password
				)
			else:
				messages.warning(request, 'Your account has been used!!!')
		else:
			messages.warning(request, 'Your password are not the same!!!')
	return render_to_response('register.html',RequestContext(request,locals()))


def home(request):
	login = request.session['login']
	return render_to_response('home.html',RequestContext(request,locals()))


def culture(request):
	login = request.session['login']
	return render_to_response('culture.html',RequestContext(request,locals()))


def center(request):
	login = request.session['login']
	return render_to_response('center.html',RequestContext(request,locals()))


def east(request):
	login = request.session['login']
	return render_to_response('east.html',RequestContext(request,locals()))


def general(request):
	login = request.session['login']
	return render_to_response('general.html',RequestContext(request,locals()))


def history(request):
	login = request.session['login']
	return render_to_response('history.html',RequestContext(request,locals()))


def login(request):
	if request.session['login']==1:
		request.session['login']=0;
		messages.warning(request, 'You have successfully logout!!!')
	if request.POST:
		account = request.POST['tbaccount']
		password = request.POST['tbpassword']
		if Logindb.objects.filter(account=account,password=password).count()==1:
			request.session['login'] = 1
			login = request.session['login']
			return render_to_response('home.html',RequestContext(request,locals()))
		else:
			messages.warning(request, 'Your account or password is wrong!!!')
			return render_to_response('login.html',RequestContext(request,locals()))
	return render_to_response('login.html',RequestContext(request,locals()))

def north(request):
	login = request.session['login']
	return render_to_response('north.html',RequestContext(request,locals()))


def south(request):
	login = request.session['login']
	return render_to_response('south.html',RequestContext(request,locals()))

	

def newinfo(request):
	login = request.session['login']
	newinfo = Newinfo.objects.all()
	return render_to_response('newinfo.html',RequestContext(request,locals()))



