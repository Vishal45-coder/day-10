# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:31:53 2020

@author: vishal
"""


try:
    f=open("abc.txt")
except:
    print("File cannot be opened")
    exit()
print(f.read())     
    