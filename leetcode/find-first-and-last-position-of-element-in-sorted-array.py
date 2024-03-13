class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binsear(nums,target,True)
        right=self.binsear(nums,target,False)
        return [left,right]
    def binsear(self,nums,target,lb):
        l,r=0,len(nums)-1
        i = -1
       
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l=mid+1
            elif nums[mid] > target:
                r=mid-1
            else:
                i=mid
                if lb:
                    r=mid - 1
                else:
                    l=mid+1
        return i                    

