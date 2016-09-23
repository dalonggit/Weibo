#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Infrastructure.forms import Form1
import json
import time

# 创建用户
def creat_user(request,User):
    # 验证参数是否法
    f = Form1(request.POST)
    # 传入参数合法
    if f.is_valid():
        set_user_information = f.cleaned_data
        # f.cleaned_data  获取到的数据格式{'username': 'sadfasdf', 'email': '123@123.com', 'password': '111'}
        # 判断用户是否已经注册过  通过用户名唯一
        try:
            # 用户存在
            # 不存在会报错
            user = User.objects.get(username=set_user_information["username"])
            return "用户名已经注册"
        except:
            # 用户不存在可以直接注册
            # 创建用户
            user = User.objects.create_user(username=set_user_information["username"],
                                            password=set_user_information["password"],
                                            email=set_user_information["email"],
                                            last_login=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            user.save()
            return "用户注册成功"
    # 传入参数不合法
    else:
        error_information = {}
        for i in f.errors:
            error_information[i] = f.errors[i][0]
        print(error_information)
        return json.dumps(error_information)

def user_login(request):
    from django.contrib import auth
    # 获取出入的值:
    try:
        # 获取用户名密码
        username = request.GET["username"]
        password = request.GET["password"]

        # 去数据库查找是否存在
        # 返回一个对象，里面包含了所有用户信息
        look_result = auth.authenticate(username=username, password=password)
        # 查找到了用户
        if look_result:
            request.session["id"] = look_result.id
            return "登录成功"
        else:
            return "登录失败"
            # 判断用户是否已经登陆
    except:
        return "参数获取不到"

