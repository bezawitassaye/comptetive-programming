class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=float("inf")

        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=nums[l]:
                res=min(res,nums[l])
                l=mid+1
                
            elif nums[mid]<nums[l]:
                res=min(res,nums[mid])
                r=mid-1
                
            
        return res            

        