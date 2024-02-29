class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
       res=[]
       for i,j in zip(weights,weights[1:]):
           res.append(i+j)
       res.sort()
       minn=sum(res[:k-1])
       maxx=sum(res[len(res)-k+1:])
       return maxx-minn





        