class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        checker=len(piles)//3
        summ=0
        for i in range(checker,len(piles),2):
            summ+=piles[i]
        return summ    
       
           



           

               
        