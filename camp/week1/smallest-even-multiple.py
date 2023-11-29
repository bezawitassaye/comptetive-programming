class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m=n*2

        for i in range(1,m+1):
            if i % 2 == 0 and i % n == 0:
                return i
            
        return 0