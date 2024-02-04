class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l=0
        r=0
        count=0
        if name[0] != typed[0]:return False
        while l<len(name) and r<len(typed):
            
            if name[l] == typed[r]:
               
                count+=1
                l+=1
                r+=1
            elif name[l] != typed[r] and  typed[r]==name[l-1]:
                r+=1  
            elif name[l] != typed[r]:
                return False
            else:
                l+=1 
            
        if count!=len(name ) or name[count-1]!= typed[len(typed)-1]:
                return False
        else:
            for j in range(r,len(typed)):
                if typed[j] !=  name[count-1]:
                   
                    return False       
        return True            
        
        