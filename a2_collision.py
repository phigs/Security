#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:52:51 2019

@author: fiji
"""
import hashlib
import string
import random
def randomString(stringLen):
    temp = string.ascii_lowercase + string.digits
    return ''.join(random.choice(temp) for i in range(stringLen))

def find_collision(n):
    dictionary = {}
    m1 = randomString(20).encode("ascii")
    hashm1 = hashlib.sha256(m1).digest()
    hashm1 = hashm1[0:n]
    dictionary[hashm1] = m1
    while True:
        m2 = randomString(20).encode("ascii")
        hashm2 = hashlib.sha256(m2).digest()
        hashm2 = hashm2[0:n]
        if hashm2 in dictionary:
            return dictionary[hashm2],m2
        if hashm2 not in dictionary:
            dictionary[hashm2] = m2