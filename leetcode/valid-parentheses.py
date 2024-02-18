class Solution:
    def isValid(self, s: str) -> bool:
        hashset={
            "(":")",
            "{":"}",
            "[":"]"
        }
        stack=[]

        for char in s:
            if char in hashset:
                stack.append(char)
            elif stack and hashset[stack[-1]] == char:
                stack.pop()
            else:
                return False    
        return len(stack) == 0            
      


        