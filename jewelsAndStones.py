# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 09:34:42 2020

@author: Einyan
"""
def numJwelsInStones(J, S):
    h = {}
    count = 0
    for i in S:
        if i not in h:
            h[i] = 1
        else:
            h[i] += 1
                      
    print(h)
    
    for j in J:
        if j in h:
            count += h[j]
    return count
        
print(numJwelsInStones("ebd", "bbb"))