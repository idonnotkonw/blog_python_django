#!/usr/bin/python
#coding:utf-8
from django import forms
import re
from django.core.exceptions import ValidationError
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class register_info(forms.Form):
	username = forms.CharField(max_length = 20,error_messages={'required': ('用户名不能为空')})
	password = forms.CharField(max_length = 16,error_messages={'required': ('密码不能为空')})
	email = forms.EmailField(error_messages={'required': ('邮箱不能为空'),'invalid': ('邮箱格式错误')})	
	phonenumber = forms.CharField(validators=[mobile_validate, ],error_messages={'required': ('手机不能为空')})

	
