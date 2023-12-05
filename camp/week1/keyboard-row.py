class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first="qwertyuiop"
        ff=0
        second="asdfghjkl"
        ss=0
        third="zxcvbnm"
        tt=0
        sss=[]
        for i in words:
            for j in i:
                if j.lower()  in first:
                    ff+=1
                elif j.lower() in second:
                    ss+=1
                elif j.lower() in third:
                    tt+=1
            if len(i) == ff or len(i) == ss or len(i)== tt:
                sss.append(i) 
            ff=0
            ss=0
            tt=0        
        return sss            




