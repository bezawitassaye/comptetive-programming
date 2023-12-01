class Solution:
    def romanToInt(self, s: str) -> int:
        hashset={
            "I":1,
            "V": 5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        count=0
        stack=[]
        for i in range(len(s)):
            if i+1 < len(s) and hashset[s[i]] < hashset[s[i+1]] :
                count+=hashset[s[i+1]]- hashset[s[i]]
                stack.append(s[i])
                stack.append(s[i+1])
            else:
                if stack and  s[i] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    count+=hashset[s[i]] 
        return count        

        