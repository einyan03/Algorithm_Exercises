# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 23:06:44 2020

@author: Einyan

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  
Return the weight of this stone (or 0 if there are no stones left.)
"""
import heapq
def lastStoneWeight(stones):
    # Make all the stones negative. We want to do this *in place*, to keep the
    # space complexity of this algorithm at O(1).
    for i in range(len(stones)):
        stones[i] *= -1

    # Heapify all the stones.
    heapq.heapify(stones)

    # While there is more than one stone left, remove the two
    # largest (i.e. smallest in the case due to the negative), 
    # smash them together, and insert the result
    # back into the heap if it is non-zero.
    while len(stones) > 1:
        stone_1 = heapq.heappop(stones)
        stone_2 = heapq.heappop(stones)
        if stone_1 != stone_2:
            heapq.heappush(stones, -(stone_1 - stone_2))

    # Check if there is a stone left to return. Convert it back
    # to positive.
    return heapq.heappop(stones) if stones else 0
    
print(lastStoneWeight([2,7,4,1,8,1]))