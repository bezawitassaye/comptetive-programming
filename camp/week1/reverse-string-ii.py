class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=k*2
        s=list(s)
        for i in range(len(s)):
            if i%n==0:
                s[i:i+k]=s[i:i+k][::-1]
        return "".join(s)
        