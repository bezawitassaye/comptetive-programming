class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1=nums[:n]
        n2=nums[n:]
       
        n3=[]
        for i in range(n):
            n3.append(n1[i])
            n3.append(n2[i])
        return n3    

        