class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last=nums[-1]
        op=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > last:
                if nums[i] % last ==0:
                    op+=(nums[i] // last) -1
                else:
                    op+=(nums[i] // last) 
                    last= nums[i] // ((nums[i]//last)+1)
            else:
                last=nums[i]  
            print(i,nums[i],last)          
        return op           
                   

