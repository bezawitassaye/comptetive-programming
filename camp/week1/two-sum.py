class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       hashprev={}

       for i,n in enumerate(nums):
           diff = target-nums[i]

           if diff in hashprev:
               return [hashprev[diff],i]
           hashprev[n]=i
       return     
        