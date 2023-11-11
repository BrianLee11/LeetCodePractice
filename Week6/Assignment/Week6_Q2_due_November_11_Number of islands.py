# Week4_due_Sat_October_28
# Question 2
# Minimum add to make parentheses valid (Medium)

class Solution(object):
    def numIslands(self, grid):
        # Helper function to perform DFS on the grid.
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # Mark the current cell as visited
            # Visit all adjacent cells
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        if not grid:
            return 0
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':  # If a land cell is found
                    num_islands += 1  # Increment the count
                    dfs(i, j)  # Perform DFS to mark all adjacent land cells
        
        return num_islands

# The function can be tested with a grid input to check if it correctly counts the islands.
