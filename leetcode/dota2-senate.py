class Solution:
    def predictPartyVictory(self, senate: str) -> str:
       S=list(senate)
       R=deque()
       D=deque()  
       for i ,c in enumerate(senate):
           if c == "R":
               R.append(i)
           else:
               D.append(i)
       while D and R:
           dt=D.popleft()
           rt=R.popleft()
           if rt < dt:
               R.append(dt+len(senate))
           else:
               D.append(rt+len(senate))
       return "Radiant" if R else "Dire"                       
                        
                        


        