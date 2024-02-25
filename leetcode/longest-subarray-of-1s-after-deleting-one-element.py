class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        an=0
        idx=[]
        i=0
        count=0
        res=[]
        if len(set(nums))==1 and nums[0]==1:
            return len(nums)-1
        while i < len(nums):
            if nums[i] == 1 and count <= 1:
                res.append(nums[i])
                i+=1
            elif nums[i] == 0 :
                count+=1
                idx.append(i)
                i+=1
            elif count > 1:
                count=0
                m=idx.pop(0)
                i=m+1
                idx=[]
                res=[]
            an = max(len(res),an) 
        return an          



        