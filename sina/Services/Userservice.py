#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc

class IUserRepertory(metaclass=abc):

    @abc.abstractmethod
    def check_login(self):
        pass

    @abc.abstractmethod
    def register(self):
        pass

    @abc.abstractmethod
    def get_user_info(self):
        pass

    @abc.abstractmethod
    def existence(self):
        pass