#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sina.settings import REDIS
import redis
import json
timeout=24*60*60

class Redis:

    def __init__(self):
        self.conn = redis.Redis(**REDIS)

    def add_login(self,user_id):

        self.conn.set('login_%s'%user_id,True,ex=timeout)

    def get_login(self,user_id):
        ret=self.conn.get('login_%s'%user_id)
        return ret

    def add_wb(self,wb_id,data):
        print(type(data))
        data['wb_id']=wb_id
        data=json.dumps(data)
        self.conn.set(wb_id,data)

    def get_wb(self,key):
        return self.conn.get(key)

    def update_user(self,user_id,data=None):
        print('update_user,data',data)
        if  not data:
            data = { 'wb_list': [], 'count': 0}
        self.conn.set('follows_%s' % user_id, json.dumps(data))

    def get_user(self,user_id):
        ret=self.conn.get('follows_%s' % user_id)
        if not ret:
            ret={ 'wb_list': [], 'count': 0}
        else:
            ret = json.loads(str(ret, encoding='utf8'))
        return ret
