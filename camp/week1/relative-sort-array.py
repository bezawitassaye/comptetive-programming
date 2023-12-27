class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3=[]
        arr4=[]
        
        for i in range(len(arr2)):
            if arr2[i] in arr1:
                n=arr1.count(arr2[i])
                arr3+=n*[arr2[i]]
        for j in arr1:
            if j not in arr3:
                arr4.append(j)
        arr4.sort()        
        return arr3  + arr4          
        
        