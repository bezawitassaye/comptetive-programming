class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        indx=nums.index(max(nums))
        stack=[]
        for i in range(indx,indx-len(nums),-1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res                    
                      



        