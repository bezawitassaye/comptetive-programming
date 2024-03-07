class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)) :
            n=nums.pop(0)
            pr=self.permute(nums)
            for perm in pr:
        
                perm.append(n)
            res.extend(pr)
            nums.append(n)
        return res           

