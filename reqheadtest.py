#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#resp = requests.head("http://www.google.com")
resp = requests.head("http://www.unitec.mx/contaduria-publica-derecho-fiscal/")

print resp.status_code
print resp.text
print resp.headers