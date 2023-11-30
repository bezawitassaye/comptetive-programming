class Solution:
    def interpret(self, command: str) -> str:
        ss=list(command)
        aa=[]
        for i in ss:
            if i == ")" and aa[-1]=="(":
                aa.pop()
                aa.append("o")
                continue
            if i == ")" and aa[-1] == "l" and aa[-2] == "a" and aa[-3] == "(":
                aa=aa[:len(aa)-3]
                aa.append("a")
                aa.append("l")
                continue
            aa.append(i) 
        return ''.join(aa)     




        
        return s            


        