class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr=[]
        for a,b in costs :
            arr.append([a-b,[a,b]])
       
        arr.sort()
        print(arr)
        count=0
        for i in range(len(arr)):
            if i < len(arr)//2:
             
                count+=arr[i][1][0]
            elif i >= len(arr)//2:
               
                count+=arr[i][1][1]
     
        return count            

        