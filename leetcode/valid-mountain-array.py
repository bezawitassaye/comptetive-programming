class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag = False
        j=len(arr) - 1
        if len(arr) < 3:
            return False
        i = 0
        while i + 1 < len(arr)-1 and arr[i] < arr[i+1]:
     
            i+=1
       
        while (j-1) >0 and arr[j] < arr[j-1]:
            j-=1
              
        return i == j                    
                    

        