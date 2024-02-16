class Solution:
    def minimumSteps(self, s: str) -> int:
        
        l=0
        r=len(s)-1
        count=0
        while l < r:
          
            if s[l] == "1" and s[r]=="0":
                count+=r-l
                l+=1
                r-=1
                print(count,l,r)
            elif s[r]!="0":
                r-=1
            elif s[l]!="1":
                l+=1 
            else:
                l+=1
                r-=1    
        return count                

        