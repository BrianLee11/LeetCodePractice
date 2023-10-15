"""
3. Longest Substring Without Repeating Characters
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Initialize a dictionary to store the index of each character's last occurrence
        last_seen = {}
        max_length = 0
        start = 0  # Start of the current substring

        # Iterate through the characters of the string using a traditional for loop
        for end in range(len(s)):
            char = s[end]

            # If the character is seen again and its last occurrence is after the start of the current substring
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1

            # Update the last seen index of the character
            last_seen[char] = end

            # Calculate the length of the current substring
            current_length = end - start + 1

            # Update the maximum length if needed
            max_length = max(max_length, current_length)

        return max_length