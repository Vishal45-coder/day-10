# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 08:50:52 2020

@author: vishal
"""


import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("file has removed")
else:
    print("file does not exists")    
if os.path.exists("Camera Roll"):
     os.rmdir("Camera Roll")    
     print("dir removed")
else:
     print("Dir  not Exists")     