# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 02:54:12 2020

@author: DELL
"""

def longestPalindrome(s):
    "with dp"
    n = len(s)  # input s length
    # table to check if the substring is palindrome
    # table[i][i] will be true if substring s[i..j] is palindrome. Otherwise, false
    table = [[0 for x in range(n)] for y in range(n)]
    
    # if one character, then always palindrom, i.e. 'a' - palindrome
    maxLength = 1
    i = 0
    while i < n:
        table[i][i] = True
        i += 1
       
    # check for substring length 2, i.e. 'ab'
    start = 0
    i = 0
    while i < n - 1: # len(s)-1 for indices
        if s[i] == s[i+1]: # if the first char is equal to the second char
            table[i][i+1] = True
            start = i
            maxLength = 2
        i += 1
      
    # check for substring more than length 2 (i.e. begin from 3rd pos -- 'abc...')
    k = 3
    while k <= n: 
        # fix the starting index
        i = 0
        while i < (n - k + 1):
            # get the ending index of substring from starting index i and length k
            j = i + k - 1
            
            # check for substring from ith index to jth inex if s[i+1] to s[j-1] is a palindrome
            if table[i+1][j-1] and s[i]==s[j]:
                table[i][j] = True
                
                if k > maxLength: 
                    start = i
                    maxLength = k
                
            i += 1
        k += 1
    return s[start:start+maxLength]

print(longestPalindrome("babad"))

"""44ms"""
def longestPalindromI(s):
    N = len(s)
    if N < 2 or s == s[::-1]: 
        return s
    mx, start = 1, 0
    for i in range(1, N):
        odd = s[i-mx-1:i+1]
        if i-mx >= 1 and odd == odd[::-1]:
            start = i-mx-1
            mx += 2
        else:
            even = s[i-mx:i+1]
            if even == even[::-1]:
                start = i-mx
                mx += 1
    return s[start:start+mx]