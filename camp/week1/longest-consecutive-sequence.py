class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        checker=1
        nums.sort()
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i +1 < len(nums):
                if nums[i]+1 == nums[i+1] :
                    checker+=1 
                elif nums[i] == nums[i+1]:
                    continue    
                else:
                    checker=1
                count=max(count,checker)    
        return count                


        
              
            


        