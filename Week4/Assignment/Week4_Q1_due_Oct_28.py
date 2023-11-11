# Week4_due_Sat_October_28
# Question 1
# Find center of star graph (Easy)

class Solution:
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        # The center node will be the only one connected to all others,
        # thus it will appear in both of the first two edges.
        # Compare the first two edges and find the common node.
        return edges[0][0] if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] else edges[0][1]

# Let's test the function with the provided examples to verify it works as expected.

# Example 1:
edges1 = [[1,2],[2,3],[4,2]]
# Example 2:
edges2 = [[1,2],[5,1],[1,3],[1,4]]

solution = Solution()
print("The center of the first star graph is:", solution.findCenter(edges1))  
# Expected output: 2

print("The center of the second star graph is:", solution.findCenter(edges2)) 
# Expected output: 1