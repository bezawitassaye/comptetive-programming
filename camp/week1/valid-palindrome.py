class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        
        while l < r:
            print(s[l],s[r])
            if s[l].isalnum() and s[r].isalnum():
                print(s[l],s[r])
                if s[l].lower() != s[r].lower():
            
                    return False
                l+=1
                r-=1
            elif  not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
        return True                  