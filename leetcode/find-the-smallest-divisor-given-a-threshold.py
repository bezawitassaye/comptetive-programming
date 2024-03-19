class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=10**6
        
        while l<=r:
            res=0
            mid=(l+r)//2
            for i in nums:
                res+=math.ceil(i/mid)
            if res <=  threshold:
                
                r=mid-1
            else:
                l=mid+1
        return l      


