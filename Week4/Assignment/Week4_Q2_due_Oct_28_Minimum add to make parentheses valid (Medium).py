# Week4_due_Sat_October_28
# Question 2
# Minimum add to make parentheses valid (Medium)

class Solution:
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0  # Tracks the balance of parentheses
        insertions = 0  # Counts the number of insertions needed
        
        for char in s:
            if char == '(':
                balance += 1  # Increment balance for every '('
            else:  # It's a ')'
                if balance == 0:
                    insertions += 1  # Need to insert a '(' before this ')'
                else:
                    balance -= 1  # Decrement balance for a matching pair
        
        # After checking all parentheses, insertions are needed for all unmatched '('
        return insertions + balance  # Total insertions are unmatched '(' plus insertions made earlier

# Test the function with the provided examples
solution = Solution()
print("Minimum insertions for '())':", solution.minAddToMakeValid("())"))  # Expected: 1
print("Minimum insertions for '(((':", solution.minAddToMakeValid("((("))  # Expected: 3
