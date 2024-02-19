class Solution:
    def scoreOfParentheses(self, s: str) -> int:
   
       stack=[]
       count=0
       for i in range(len(s)):
           if s[i] =="(":
               stack.append(count)
               count=0
           else:
               if stack:
                   count=stack.pop()+max(2*count,1)
       return count                                    

        