class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize a dictionary to keep track of the count of each character
        alphabets = {}

        # Initialize variables for the answer, left pointer, and right pointer
        ans = 0
        left = 0
        right = 0

        # Iterate through the string using the right pointer
        for right in range(len(s)):
            # Update the count of the current character in the dictionary
            alphabets[s[right]] = 1 + alphabets.get(s[right], 0)

            # Check if the current window size minus the count of the most frequent character
            # is greater than the allowed replacements (k)
            if (right - left + 1) - max(alphabets.values()) > k:
                # If so, move the left pointer and decrease the count of the character at the left
                alphabets[s[left]] -= 1
                left += 1
            else:
                # Update the answer with the maximum window size
                ans = max(ans, (right - left + 1))

        # Return the final answer
        return ans