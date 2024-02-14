class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr=[]
        if numNegOnes:
            arr+=[-1]*numNegOnes
        if  numZeros:
            arr+=[0]*numZeros  
        if  numOnes:
            arr+=[1]*numOnes
        return sum(arr[len(arr)-k:])          