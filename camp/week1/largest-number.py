from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: str, y: str) -> int:
            xy = x + y
            yx = y + x
            return int(xy) - int(yx)
        
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        
        return str(int(''.join(nums)))