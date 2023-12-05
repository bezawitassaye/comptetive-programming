class Solution:
    def numberOfMatches(self, n: int) -> int:
        count=0
        x=n
        
        for i in range(x):
            if n > 1:
                count+=n//2
                n=n-n//2
            else:
                break
        return count


