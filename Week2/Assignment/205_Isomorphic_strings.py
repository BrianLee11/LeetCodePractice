"""
LeetCode practice
Number: 205. 
Title: Isomorphic Strings
Difficulty: Easy
Related topics: 1) hash table, 2) string
"""

class Solution(object):
    def isIsomorphic(self, input_string1, input_string2):
        """
        :input type input_string1: str
        :input type input_string2: str
        :return type: bool
        """
        
        # trivial case:
        if len(input_string1) != len(input_string2):
            return False
        
        # non-trivial case
        else: 

            # Initialize an empty hash table (dictionary)
            letter_count_hash1 = {}
            letter_count_hash2 = {}
            
            # Iterate through the characters in the input string
            for letter in input_string1:
                # Use the letter as the key in the hash table and increment the count
                # letter_count_hash1.get(letter, 0) means get the value of 'letter'. 
                # If the key is found in the dictionary, it returns the corresponding value. 
                # If the key is not found in the dictionary, it returns the default value, 
                    # which in this case is 0. 
                letter_count_hash1[letter] = letter_count_hash1.get(letter, 0) + 1
    
            for letter in input_string2:
                letter_count_hash2[letter] = letter_count_hash2.get(letter, 0) + 1
    
            # Print the letter counts
            # example: this dictionary has data structure {'e': 1, 'g': 2} 
    
            # Extract the values from each dictionary
            values1 = list(letter_count_hash1.values())
            values2 = list(letter_count_hash2.values())
    
            # Sort the value lists to make the comparison order-independent
            values1.sort()
            values2.sort()
    
            # Check if the values are the same
            if values1 == values2:
                print("The dictionaries have the same values.")
                return True
            else:
                print("The dictionaries have different values.")
                return False
        
# Example usage:
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # True
print(solution.isIsomorphic("foo", "bar"))  # False
print(solution.isIsomorphic("paper", "paper"))  # True


