class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=0
        r=0
        g.sort()
        s.sort()
        count=0
        if len(s) ==0:
            return 0
        while l < len(g) and r<len(s) :
            
            while r< len(s):
                if g[l]<=s[r]:
                    print(g[l],s[r])
                    count+=1
                    r+=1
                    break
                r+=1    
            l+=1
           
        return count        
        