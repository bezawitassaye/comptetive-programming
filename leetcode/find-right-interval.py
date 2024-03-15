class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        fin=[]
        for i,j in enumerate(intervals):
           j.append(i)
           fin.append(j)
        fin.sort()   
        res=[-1]*len(intervals)

        for k in range(len(fin)):
            self.checker(fin,res,fin[k][1],k)
        return res
    def checker(self,fin,res,target,k):
        l=0
        r=len(fin)-1
        while l<=r:
            mid=(l+r)//2    
            if fin[mid][0]>=target:
                res[fin[k][2]]=fin[mid][2]
                r=mid-1
            else:
                l=mid+1    
