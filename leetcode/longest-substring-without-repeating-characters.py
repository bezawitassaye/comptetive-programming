class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        res=0
        i=0
        j=0
        
        while j < len(s):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            hashset.add(s[j])
            j+=1 
            res=max(res,len(hashset))
        return res
       

        