# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 02:27:14 2020

@author: Einyan
"""


"""
If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.
Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def maxProfit1(prices):
    if not prices: # empty
        return 0
    
    max_profit = 0 
    min_value = prices[0]
    
    for i in range(1, len(prices)):
        if prices[i] < min_value: 
            min_value = prices[i]   # update minimum with the current lesser price
        else:
            max_profit = max(max_profit, prices[i] - min_value)
            
    """0 for no profit as there is no addition due to lesser prices in the range whereas
    maximum profit being updated in the result for larger selling prices"""
    return max_profit     

print(maxProfit1([7,1,5,3,6,4]))

"""
as many trasactions as you like 
Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""
def maxProfit2(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit