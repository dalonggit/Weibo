#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect,HttpResponse

def index(request):

    return render(request,'index.html')

def home(request):

    return render(request,'logined_index.html')