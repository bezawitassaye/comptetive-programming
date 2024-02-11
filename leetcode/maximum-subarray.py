class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr=[]
        count=nums[0]
        maxx=0
        for i in range(1,len(nums)):
            if count  < nums[i] and count<0:
                count=nums[i]
            else:
                
                arr.append(count)
                count+=nums[i]
            arr.append(count)
            
            
                
            
        if arr:
            return max(arr)
        else:
            return nums[0]            
