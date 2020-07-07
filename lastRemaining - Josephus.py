# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:06:42 2020

@author: Einyan
"""

def lastRemaining(n):
    N = n   # number of remaining numbers
    fwd = True   # flag for forward/backward elimination
    m = 2    # elimination step/interval
    s = 0   # elimination base

    while N > 1:
        if fwd or N % 2 == 1: 
            s += m // 2
        m *= 2
        N = N // 2
        fwd = not fwd   # reverse the pass direction
    return s+1

print(lastRemaining(9))