# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 18:57:37 2020

@author: dell3542
"""

import requests
data =requests.get('https://www.kau.edu.sa/Home.aspx')

file = open('url content.txt','w')
file.write(data.text)
file.close()

with open('url content.txt','r') as file:
    file_contents=file.read()
    print(file_contents)