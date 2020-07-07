# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:11:11 2020

@author: Einyan
"""

def lastStoneWeightII(stones):
    total = sum(stones)
    stones = sorted(stones)
    dp = set([0])
    res = total
    for x in stones:
        tmp = set(dp)
        for y in dp:
            tmp.add(y + x)
        dp = tmp
    dp.remove(0)
    for s in dp:
        if s < total / 2:
            res = min(res, total - s - s)
        else:
            res = min(res, s - (total - s))
    return res

"""
    total = sum(stones)
    start = min(stones)
    dp = [False] * (total//2 + 1)
    dp[0] = True
    for s in stones:
        for i in range(total//2, start-1, -1):
            if s<=i and dp[i-s]:
                dp[i] = True

    for i in range(len(dp)-1, -1, -1):
        if dp[i]:
            return abs(2*i-total)
"""