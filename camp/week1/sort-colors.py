class Solution:
    def sortColors(self, nums: List[int]) -> None:
        nums.sort()
        r=1
        color=0
        count=0
        l=0
        while r < len(nums):
            if nums[l] != color:
                if nums[r] == color:
                    nums[l],nums[r] = nums[r],nums[l]
                    count+=1
                    l+=1
                    r+=l
                elif nums[r] == color:
                     r+=l    
                elif count==2:
                    color+=1
                    count=0
            
            l+=1
            r+=1


