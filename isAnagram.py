# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 04:24:14 2020

@author: DELL
"""

def isAnagram(s, t):
    return (''.join(sorted(s)) in ''.join(sorted(t)))

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))

def merge(nums1, nums2):
    index = 0
    for i,num in enumerate(nums1):
        if num == 0:
            nums1[i] = nums2[index] 
            index += 1
    return(nums1)
    
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6],      
print(merge(nums1, nums2))