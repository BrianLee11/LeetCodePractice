class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        # List to store the final level order traversal
        levels = []
        
        # If the tree is empty, return an empty list
        if not root:
            return levels
        
        # Initialize a queue with the root node
        from collections import deque
        queue = deque([root])
        
        # Perform BFS
        while queue:
            # List to store the current level's values
            level = []
            # Number of nodes in the current level
            level_length = len(queue)
            
            for i in range(level_length):
                # Pop the node from the queue
                node = queue.popleft()
                # Add the node's value to the level list
                level.append(node.val)
                # Add the node's children to the queue if they exist
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            
            # Add the current level's values to the levels list
            levels.append(level)
        
        # Return the level order traversal
        return levels