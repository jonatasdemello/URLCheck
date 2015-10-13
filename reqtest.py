#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# r = requests.get('https://api.github.com', auth=('user', 'pass'))
r = requests.get('http://www.google.com')

print r.status_code
print r.headers['content-type']

# ------
# 200
# 'application/json'
