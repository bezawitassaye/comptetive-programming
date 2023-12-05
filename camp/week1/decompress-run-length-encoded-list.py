class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ss=[]
        aa=[]
        for i in range(0,len(nums)+1,2):
            ss.append(i)
        for i in range(len(ss)-1):
            for j in range(nums[ss[i]]):
                aa.append(nums[ss[i+1]-1])

        return aa      