class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i=1
        j=0
        ss,pp={},{}
        res=[]
        n=len(s)
        n1=len(p)
        if len(p) > len(s):
            return []
        for k in range(len(p)):
            pp[p[k]] = 1 + pp.get(p[k],0)
            ss[s[k]] = 1 + ss.get(s[k] , 0)
        if ss == pp:
            res.append(0)
        while i < (n-n1)+1:
          
            ss[s[i-1]]-=1
            if ss[s[i-1]] ==0:
                ss.pop(s[i-1])
            ss[s[i]] = ss.get(s[i] , 0)
            ss[s[i+n1-1]] =  1 + ss.get(s[i+n1-1] , 0)
            if ss == pp:
                res.append(i)
            i+=1
        return res    
            
          
               
                
           
               
       
                    

                

        