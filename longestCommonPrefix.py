# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 01:30:13 2020

@author: Einyan
"""

def longestCommonPrefix(strs):   
    if len(strs) == 0:
        return ""

    # 1: look for the shorted string among the array
    min_len = len(strs[0]) # step 1: take strs[0] length
    for i in range(len(strs)): # step 2: traverse thru the array to compare and find the shortest
        min_len = min(min_len, len(strs[i]))

    # 2: 2D array 
    longCPrefix = ""
    i = 0  
    while i < min_len:  # this is to go only up to the positions of shortest length
        char = strs[0][i] # first index of first ele in the array
        for j in range(1, len(strs)): # first index of second, third, ... ele in the array
            if strs[j][i] != char: # if not same, then empty string
                return longCPrefix

        longCPrefix = longCPrefix + char # concat the new found char in lcp
        i += 1 # increment i by 1

    return longCPrefix

print(longestCommonPrefix(["car", "current", "circuit"]))