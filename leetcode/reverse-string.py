class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(s,start,end):
            
            if start<len(s)//2:
                s[start],s[end] = s[end],s[start]
                reverse(s, start+1,end-1 )
        reverse(s,0,len(s)-1)        

             
        