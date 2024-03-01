class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1={}
        set2={}
        for i in s1:
            set1[i] = 1 + set1.get(i,0)
        j=0

        while j <= len(s2) - len(s1):
            for k in range(j,j+len(s1)):
                set2[s2[k]] = 1 + set2.get(s2[k],0)
            print(set2)    
            if set1 == set2:
                return True
            set2={}
            j += 1
        return False            
                


   
