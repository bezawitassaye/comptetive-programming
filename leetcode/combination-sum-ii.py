class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       candidates.sort()
       res=[]

       def back(cur,pos,target):
           if target ==0:
               res.append(cur.copy())
           if target <= 0:
               return
           prev=-1
           for i in range(pos,len(candidates)):
               if candidates[i] == prev:
                   continue
               cur.append(candidates[i])
               back(cur,i+1,target - candidates[i])
               cur.pop()
               prev=candidates[i]
       back([],0,target) 
       return res                   