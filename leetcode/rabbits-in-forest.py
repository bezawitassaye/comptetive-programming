class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashset={}
        count=0
   
        for i in answers:
            hashset[i]=1+hashset.get( i,0)  
        print(hashset)    
        for  j in hashset:
            
              count+=hashset[j]- (hashset[j] % (j+1))
              if (hashset[j] % (j+1)):
                  count+=j+1
        return count          


              
                    

        



        