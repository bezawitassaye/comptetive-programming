class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        nn=uu=sum(nums[:k])

        for i in range(k,len(nums)):
            uu+=nums[i]-nums[i-k]
            nn=max(nn,uu)
        return nn/k    
