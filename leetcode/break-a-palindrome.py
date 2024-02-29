class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        p=list(palindrome)
        if len(p)==1:
            return ""
        for i in range(len(p)):
            if p[i] != "a":
                p[i]="a"
                break  
        if p!=p[::-1]:  return "".join(p)
        p=list(palindrome)
        for j in range(len(p)-1,-1,-1):
            print(p[j])
            if p[j] == "a":
                p[j]="b"
                break
        print(p)        
        return "".join(p)        
