class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
     
        pointer=0
        ca=capacity

        for i in range(len(plants)):
            if ca < plants[i]:
                pointer+= i*2 
                ca = capacity
       
            pointer+=1
            ca -= plants[i]
           
            
        return pointer            
           

               
        