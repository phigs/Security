#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 16:36:30 2019
@author: fiji
"""
def hammingdistance(hex1, hex2):
    H1 = format(int(hex1,16),'#034b')
    H2 = format(int(hex2,16),'#034b') 
    H1.rjust(200,'0')
    H2.rjust(200,'0')
    numdif = 0
    i = 0
    while (i < len(H1)):
        if H1[i] != H2[i]:
            numdif += 1;
        i+= 1
    return(numdif)
    