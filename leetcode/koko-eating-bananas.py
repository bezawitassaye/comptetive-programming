class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l <= r:
            mid=(l+r)//2
            hou=0
            for j in piles:
                hou+=math.ceil(j/mid)
            if hou <= h:
                res=min(res,mid)
                r=mid-1
            else:
                l=mid + 1
        return res               

        