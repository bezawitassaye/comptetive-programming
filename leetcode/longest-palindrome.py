class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset={}
        res=0
        maxx=0
        for i in s:
            hashset[i] = 1 + hashset.get(i,0)
        for i in hashset:
            res+=hashset[i] // 2* 2
            maxx=max(maxx,hashset[i]%2)
        return res+maxx              

        