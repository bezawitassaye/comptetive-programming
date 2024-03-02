class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i,j,k=0,0,0
        m=len(nums)
        while k < n:
            if i < m and nums[i] <= k+1:
                k += nums[i]
                i += 1
            else:
                j+=1
                k+=(k+1)
        return j           
                    