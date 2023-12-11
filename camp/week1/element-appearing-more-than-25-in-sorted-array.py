class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hashset={}
      
        for i in arr:
            if i not in hashset:
                hashset[i]=1
            else:
                 hashset[i]+=1
            
        checker=round(len(arr)/4)
      
        for key , value in hashset.items():
            if value >checker:
                return key
        else:
            for key , value in hashset.items():
                if value == checker:
                    return key

        
               
