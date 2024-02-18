class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res=[]
        for i in range(len(arr)):
            maxx=max(arr[:len(arr)-i])
            max_idx = arr.index(maxx)+1
            arr[:max_idx] = reversed(arr[:max_idx])
            res.append(max_idx)
            arr[:len(arr)-i]=reversed(arr[:len(arr)-i])
            res.append(len(arr)-i)
        return res    

        
