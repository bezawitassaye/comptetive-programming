class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r

        def istrue(mid):
            nships,curval=1,mid
            for j in weights:
                if curval - j<0:
                    nships+=1
                    curval=mid
                curval-=j
            return nships <= days             
        while l<=r:
            mid=(l+r)//2
            if istrue(mid):
                res=min(res,mid)
                r=mid-1
            else:
                l=mid+1
        return res            
        