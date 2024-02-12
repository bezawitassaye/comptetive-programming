class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
     
       hashset={}
       hashset[0]=1
       count=0
       checker=0
       total=0
       for i in range(len(nums)):
           count+=nums[i]
           diff=count-k

           if diff  in hashset:
               checker+=hashset[diff]
           
           if count in hashset:
               hashset[count]+=1
          
           if count not in hashset:
               hashset[count]=1
       print(hashset)
       return checker                 
