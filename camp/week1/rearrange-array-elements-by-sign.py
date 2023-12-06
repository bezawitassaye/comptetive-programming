class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative=[]
        postive=[]
        rearranging=[]
        for i in nums:
            if i < 0:
                negative.append(i)
            else:
                postive.append(i)
        n=len(nums)//2
        for j in range(n):
            rearranging.append(postive[j])
            rearranging.append(negative[j])
        return rearranging    




        