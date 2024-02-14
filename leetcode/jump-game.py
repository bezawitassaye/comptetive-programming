class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count=0
        for num in nums:
            if count<0:
                return False
            elif num>count:
                count=num
            count-=1
        return True            