class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)):
            if i + 1 and i+2 < len(nums):
                if nums[i] + nums[i+1] > nums[i+2]:
                    count= nums[i] + nums[i+1] + nums[i+2]
                    
        return count            


        