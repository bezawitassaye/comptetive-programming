class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack=[0]
        out=[0]*len(temperatures)
        for i in range(1,len(temperatures)):
            while stack:
                if temperatures[stack[-1]] < temperatures[i]:
                    out[stack[-1]]=i-stack[-1]
                    stack.pop()
                else:
                    break    
            stack.append(i) 
        return out      
                

            
                
        