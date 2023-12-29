class Solution:
    def sortSentence(self, s: str) -> str:
        x= s.split()
        arr=[0]*len(x)
        
        for i in range(len(x)):
            k=int(x[i][len(x[i])-1])-1
            arr[k]=x[i][0:len(x[i])-1]
        return " ".join(arr)
            
        