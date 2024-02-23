class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr=[]
        for a,b in costs :
            arr.append([a-b,[a,b]])
       
        arr.sort()
        print(arr)
        count=0
        n=len(arr)//2
        for i in range(len(arr)):
            if i < n:
                count+=arr[i][1][0]
            elif i >= n:
               
                count+=arr[i][1][1]
     
        return count            

        