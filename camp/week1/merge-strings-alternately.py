class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1=list(word1)
        word2=list(word2)
        ss=""
        while word1 and word2:
            sa=word1.pop(0)
            ss+=sa
            sb=word2.pop(0)
            ss+=sb
        
        for i in word1:
            ss+=i
        for j in word2:
            ss+=j            
        return ss
        