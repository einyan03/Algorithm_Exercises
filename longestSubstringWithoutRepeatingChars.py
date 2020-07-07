# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:00:19 2020

@author: DELL
"""

def lengthOfLongestSubstring(s):
    subS = {}
    cur_start = cur_len = longest = 0        
    
    for i, letter in enumerate(s):
        if letter in subS and subS[letter] >= cur_start:
            cur_start = subS[letter] + 1
            cur_len = i - subS[letter]
            subS[letter] = i
        else:
            subS[letter] = i
            cur_len += 1
            if cur_len > longest:
                longest = cur_len
                
    return longest

print(lengthOfLongestSubstring("abcabcbb"))