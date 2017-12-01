from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, HttpResponse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django import forms
from .models import  Article
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class UserForm(forms.Form):
	username = forms.CharField(label='用户名')
	password = forms.CharField(label='密码', widget=forms.PasswordInput)

def login_validate(request,username,password):
    rtvalue = False
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return True
    return rtvalue

def login(request):
	error = []

	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			# 获得表单数据
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']
			# 获取的表单数据与数据库进行比较
			if login_validate(request, username, password):
				
				# 已为注册用户，进行登录跳转user页面
				response = render_to_response('user.html', {'userform': userform})
				# 将username写入浏览器cookie,失效时间为3600
				response.set_cookie('username', username, 36000)
				return response
			else:
				#未注册用户进行注册
				error.append('您还未注册，现在为您注册')
				
				user = User.objects.create_user(username, password)
				user.save()
				login_validate(request, username, password)
				
				response = render_to_response('user.html', {'userform': userform})
				# 将username写入浏览器cookie,失效时间为3600
				response.set_cookie('username', username, 36000)
				return response
				#输入不合法，提示错误
		else:
			error.append('')
	
	else:
		userform = UserForm()
	return render(request, 'login.html', {'userform': userform,'error': error})

#@login_required
def user(request):
	q = request.GET.get('q')
	error_msg = ''
	if not q:
		error_msg = '请输入关键词'
		return render(request,'search_result.html', {'error_msg': error_msg})
	
	post_list = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
	
	return render(request,'search_result.html', {'error_msg': error_msg, 'post_list': post_list})

def logout_view(req):
    auth_logout(req)
    return redirect('/login/')


#@login_required
def main(req):
	return render_to_response('main.html')



	


# Create your views here.
