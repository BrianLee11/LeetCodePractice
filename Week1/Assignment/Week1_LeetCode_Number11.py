#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
LeetCode practice
Number 11. Container With Most Water
"""

"""
Question: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

"""
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Example 2:
Input: height = [1,1]
Output: 1
"""

"""
pseudo-codes
area = 0
for each i from 0 to len(height) - 1 do:
    for each j from i+1 to len(height)  1 do:
        delta_x = j - i
        delta_y = min(height[j], height[i]) 

        if area < delta_x * delta_y then:
            area = delta_x * delta_y
"""

# Written in Python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                delta_x = j - i
                delta_y = min(height[j], height[i])

                if area < delta_x * delta_y:
                    area = delta_x * delta_y
        
        return area


# In[2]:


# Create an instance of Solution
solver = Solution()

# Example 1
height = [1,8,6,2,5,4,8,3,7]

# Use the instance to call containsDuplicate
print(solver.maxArea(height))  # Output: 49


# In[3]:


# Create an instance of Solution
solver = Solution()

# Example 2
height = height = [1,1]

# Use the instance to call containsDuplicate
print(solver.maxArea(height))  # Output: 1


# In[ ]:




