#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:29:25 2019

@author: fiji
"""
import hashlib
import string
import random
def randomString(stringLen):
    temp = string.ascii_letters + string.digits
    return ''.join(random.choice(temp) for i in range(stringLen))

def find_preimage(target, n):
    while True:
        word = randomString(20).encode("ascii")
        temp = hashlib.sha256(word).digest()
        if target[0:n] == temp[0:n]:
            return word