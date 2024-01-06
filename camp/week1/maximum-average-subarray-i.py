class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      cc=nn=sum(nums[:k])
      for i in range(k,len(nums)):
          nn+=nums[i] - nums[i-k]
          cc=max(nn,cc)
      return cc/k    