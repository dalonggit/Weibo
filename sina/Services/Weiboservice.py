#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc

class IWeiboRepertory(metaclass=abc):

    @abc.abstractmethod
    def add_weibo(self):
        pass

    @abc.abstractmethod
    def get_weibo_by_userid(self):
        pass

    @abc.abstractmethod
    def get_weibo_follow(self):
        # 获取我关注人的微博，根据自己的id 首页使用
        pass

    @abc.abstractmethod
    def get_weibo_hot(self):
        # 获取热门微博
        pass

    @abc.abstractmethod
    def search_weibo(self):
        pass