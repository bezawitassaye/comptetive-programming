class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pr=[None]*len(nums)
        pr[0]=nums[0]
        for i in range(1,len(nums)):pr[i]=pr[i-1]+nums[i]
        su=[None]*len(nums)
        su[len(nums)-1]=nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):su[i]=su[i+1]+nums[i]
        return [(nums[i]*(i+1)-pr[i])+su[i]-nums[i]*(len(nums)-i) for i in range(len(nums))]