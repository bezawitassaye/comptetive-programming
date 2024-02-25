class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        hashset=set(nums)
        print(hashset)
        i=0
        j=0
        res=set()
        count=0
        while i <= len(nums) - len(hashset):
            while j < len(nums):
                res.add(nums[j])
                if len (res) == len(hashset):
                    count+=1
                j+=1    
                 
            i+=1
            j=i 
            res=set() 
        return count       


