class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        start =1 
        res=0
        while target > 1:
            if target % 2 == 0 and maxDoubles :
                res+=1
                target//=2
                maxDoubles-=1
            elif target % 2 == 0 and not(maxDoubles):
                res+=target-1
                target-=target-1
            elif target % 2 != 0 and not(maxDoubles):
                res+=target-1
                target-=target-1
            else:
                res+=1
                target-=1
        return res           






        