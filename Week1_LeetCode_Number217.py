#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
LeetCode practice
Number 217. Contains Duplicate
"""

"""
Given an integer array "nums", return true if any value appears at least twice in the array, and return false if every element is distinct

pseudco-codes

input: an array 'nums'
output: boolean (True or False)

for each i from 0 to len(nums)-1 do:
    for each j from i+1 to len(nums)-1 do:
        if nums[i] == nums[j] then:
            found = True
            break
        
    if found = True then:
        break 

return found
"""

"""
Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        found = False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    found = True
                    break
            if found:
                break
        return found


# In[6]:


# Create an instance of Solution
solver = Solution()

# Example 1
nums = [1,2,3,1]

# Use the instance to call containsDuplicate
print(solver.containsDuplicate(nums))  # Output: True


# In[7]:


# Create an instance of Solution
solver = Solution()

# Example 2
nums = [1,2,3,4]

# Use the instance to call containsDuplicate
print(solver.containsDuplicate(nums))  # Output: False


# In[8]:


# Create an instance of Solution
solver = Solution()

# Example 3
nums = [1,1,1,3,3,4,3,2,4,2]

# Use the instance to call containsDuplicate
print(solver.containsDuplicate(nums))  # Output: True


# In[ ]:




