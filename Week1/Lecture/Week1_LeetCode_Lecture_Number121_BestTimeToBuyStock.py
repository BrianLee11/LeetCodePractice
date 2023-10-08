#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
LeetCode practice
121. Best Time to Buy and Sell Stock
"""

"""
Question:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

"""
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""
pseudo codes

profit = 0

for i from 0 to len(prices)-1 do:
    for j from i+1 to len(prices) do:
        profit = max(profit, prices[j] - prices[i])

return profit
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i+1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
    
        return profit


# In[2]:


# Create an instance of Solution
solver = Solution()
prices = [7,1,5,3,6,4]

print(solver.maxProfit(prices)) # output: 5


# In[3]:


# Create an instance of Solution
solver = Solution()
prices = [7,6,4,3,1]

print(solver.maxProfit(prices))# output: 0


# In[ ]:




