class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashset={}
        count=0
   
        for i in answers:
            hashset[i]=1+hashset.get( i,0)  
        for  j in hashset:
            if hashset[j] <= j:
                count+=j+1
            elif j==0:
                count+=hashset[j]
            elif hashset[j] > j:
              count+=hashset[j]- (hashset[j] % (j+1))
              if (hashset[j] % (j+1)):
                  count+=j+1
        return count          


              
                    

        



        