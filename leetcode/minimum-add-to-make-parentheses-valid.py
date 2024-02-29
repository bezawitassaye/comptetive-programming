class Solution:
    def minAddToMakeValid(self, s: str) -> int:
   
        l=r=add=0
        for i in s:
            if i == "(":
                l+=1
            else:
                if r < l:
                    r+=1
                else:
                    add+=1
        add+=l-r
        return add               


        