class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def backtrack(i,sub):
            if i==len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            backtrack(i+1,sub)
            sub.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,sub)
        backtrack(0,[])
        return res            