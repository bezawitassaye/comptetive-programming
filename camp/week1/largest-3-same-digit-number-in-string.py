class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest_good_integer = ""
        
        for i in range(len(num) - 2):
            substr = num[i:i+3]
            if len(set(substr)) == 1:
                largest_good_integer = max(largest_good_integer, substr)
        
        return largest_good_integer