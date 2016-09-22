#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Services.Weiboservice import IWeiboRepertory
from Repertory import models

class Weibo(IWeiboRepertory):

    def add_weibo(self):
        pass

    def get_weibo_by_userid(self):
        pass

    def get_weibo_follow(self):
        # 获取我关注人的微博，根据自己的id 首页使用
        pass

    def get_weibo_hot(self):
        # 获取热门微博
        pass

    def search_weibo(self):
        pass
