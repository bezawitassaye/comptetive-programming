class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      num=[]
      co=0
      for i in nums:
          co+=i
          num.append(co)
      return  num   
