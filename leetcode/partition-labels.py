class Solution:
    def partitionLabels(self, s: str) -> List[int]:
       hashset={}
       for i in range(len(s)):
            hashset[s[i]]=i
       
       res=[]
       start=0
       end=0
       for i in range(len(s)):
           end=max(end,hashset[s[i]])
           if i ==  end:
               res.append(end - start +1)
               start=i+1
           
       return res           
        