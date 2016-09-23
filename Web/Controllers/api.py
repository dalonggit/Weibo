#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponse
from Infrastructure.myredis import Redis
import json
redis=Redis()
def new(request):
    if request.method == "POST":
        result={'status':False,'wb_list':[]}
        user_id = request.POST.get('user_id', None)
        ret=redis.get_user(user_id)
        count=ret['count']
        if ret['count'] !=0:
            result['status']=True
            for i in ret['wb_list'][0:count]:
                wb=redis.get_wb(i)
                result['wb_list'].append(wb)
            ret['count']=0
            redis.update_user(user_id,ret)
        return HttpResponse(json.dumps(result))

def count(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id', None)
        ret = redis.get_user(user_id)
        return ret['count']

