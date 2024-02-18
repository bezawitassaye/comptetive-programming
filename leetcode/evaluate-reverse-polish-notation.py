class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ss=[]
        aa=["+","-","*","/"]
        for i in tokens:
            if i not in aa:
                ss.append(int(i)) 
            else:
                if i == "+":
                   u=ss.pop()
                   v=ss.pop()
                   ss.append(v+u)
                if i == "-":
                    u=ss.pop()
                    v=ss.pop()
                    ss.append(v-u)
                if i == "*":
                    u=ss.pop()
                    v=ss.pop()
                    ss.append(v*u) 
                if i == "/":
                    u=ss.pop()
                    v=ss.pop()
                    ss.append(int(v/u))
                    

        return ss[0]                   

        