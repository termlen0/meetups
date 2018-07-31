#!/usr/bin/env python

import requests

url = "http://dynamicinventory-demo.s3.amazonaws.com/inventory.json"
data = requests.get(url)

print(data.text)
