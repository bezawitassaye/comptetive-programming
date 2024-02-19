from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res=[]
        res=deque(res)
        for i in range(len(deck)-1,-1,-1):
           
            if len(res)<2:
                res.appendleft(deck[i])
               
            else:
                m=res.pop()
                res.appendleft(m)
                res.appendleft(deck[i])
        return list(res)
                  


