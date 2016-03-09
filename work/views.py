#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,render_to_response
from work.models import userinfo,bloginfo
from django.http  import HttpResponseRedirect,HttpResponse
from work import html_helper,common,forms
import json
# Create your views here.
def login(request):
	inf={'status':''}
	if request.method == 'POST':
		username = request.POST.get('username',None)
		password = request.POST.get('password',None)
		is_empty = all([username,password])
		if is_empty:
			count = userinfo.objects.filter(username=username,password=password).count()
			if count == 1:
				request.session['is_login']={'username':username}
				return HttpResponseRedirect('/index/')
				
			else:
				inf['status'] = '用户名或密码错误'
 		else:
			inf['status'] = '用户名或密码不能为空'
	return render_to_response('login.html',inf)

def add(request):
	
	user_dict = request.session.get('is_login',None)
	print user_dict
	if user_dict:
		if request.method == 'POST':

			headline=request.POST.get('headline',None)
			author=request.POST.get('author',None)
			text=request.POST.get('text',None)
			bloginfo.objects.create(headline=headline,author=author,text=text)
		
			return HttpResponseRedirect('/index/')
		return render_to_response('add.html')
	else:
		return HttpResponseRedirect('/login/')
def index(request,page):
	page = common.try_int(page,1)
	count = bloginfo.objects.all().count()
	pageobj = html_helper.PageInfo(page,count)
	
	result = bloginfo.objects.all()[pageobj.start:pageobj.end]
	page_string = html_helper.Pager(page,pageobj.all_page_count)
	ret = {'data':result,'count':count,'page':page_string,'username':''}
	user_dict = request.session.get('is_login',None)
	
	if user_dict:
		ret['username']=user_dict['username']

		return render_to_response('index.html',ret)
	else:
		return HttpResponseRedirect('/login/')
def register(request):
	obj = forms.register_info()
	ret = {'data':obj,'error':'','register':''}
	
	
	if request.method == 'POST':
		CheckForm = forms.register_info(request.POST)
		
		if CheckForm.is_valid():
			username = request.POST.get('username',None)

			count = userinfo.objects.filter(username=username).count()
			if count == 0:
				password = request.POST.get('password',None)
				email = request.POST.get('email',None)
				phonenumber = request.POST.get('phonenumber',None)
				userinfo.objects.create(username=username,password=password,email=email,phonenumber=phonenumber)
				ret['register']='注册成功'
				return render_to_response('login.html',ret)
					
			else:
				ret['error'] = '用户名已存在'
			
		else:
			error_msg = CheckForm.errors.as_data().values()[0][0].messages[0]
				
			ret['error'] = error_msg
			ret['data'] = CheckForm		
			
	return render_to_response('register.html',ret)

def logout(request):
	del request.session['is_login']
	return HttpResponseRedirect('/login/')
