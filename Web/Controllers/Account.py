#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse
from Services import Login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate,login
from Infrastructure.myredis import Redis

# def  login_test(request):
#     if request.method == "POST":
#         username = request.POST.get('username',None)
#         password = request.POST.get('password',None)
#         auth_ret=authenticate(username=username,password=password)
#         if auth_ret:
#             r_obj=REDIS()
#             r_obj.add_login(auth_ret.userprofile.id)
#             return redirect('/')
#         else:
#             error='用户名密码不匹配'
#             return render(request,'index/login.html',{'error':error})
#     else:
#         return render(request,'index/login.html',{'error':''})
def login(request):
    """
    使用方法
    POST 提交username，password，email 注册用户
    GET  提交username，password  用户名密码验证，验证成功写入session
    OPTION 用户注销

    """
    # 用户把微博提交过了
    # 创建用户
    if request.method == "POST":
        caret_result = Login.creat_user(request,User)
        return HttpResponse(caret_result)

    # 用户登录
    if request.method == "GET":
        login_result = Login.user_login(request)
        return HttpResponse(login_result)