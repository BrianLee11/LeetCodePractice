from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Build a frequency map
        count = Counter(nums)
        
        # Use a heap to find the k most frequent elements
        # The heap elements are inverted (frequency, number) tuples so that the smallest frequency is at the top
        return heapq.nlargest(k, count.keys(), key=count.get) # uses the count.get function to sort the keys by their frequency