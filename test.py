#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

r=redis.Redis(host='192.168.11.76',db=0)
r.set()