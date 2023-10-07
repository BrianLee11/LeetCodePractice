#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
LeetCode practice
Number 239. Sliding Window Maximum
"""

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""

"""
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


"""
pseudo codes

array = []
for i from 0 to len(nums) - k do:
    # slicing
    temp = []
    for j from i to i + 2 do:
        temp.append(nums[j])
    
    # compute the maximum element of temp
    max = temp.max()

    #append to the array
    array.append(max)

return array
"""

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        array = []
        for i in range(len(nums) - k + 1):
            temp = []
            for j in range(i, i+k):
                temp.append(nums[j])
        
            max_value= max(temp)
            array.append(max_value)
    
        return array


# In[4]:


# Create an instance of Solution
solver = Solution()

# Example 1
nums = [1,3,-1,-3,5,3,6,7]
k = 3

# Use the instance to call containsDuplicate
print(solver.maxSlidingWindow(nums, k))  # Output: [3,3,5,5,6,7]


# In[5]:


# Create an instance of Solution
solver = Solution()

# Example 2
nums = [1]
k = 1

# Use the instance to call containsDuplicate
print(solver.maxSlidingWindow(nums, k))  # Output: [1]


# In[ ]:




