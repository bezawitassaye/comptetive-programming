class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        numone=set(nums1)
        for i in nums2:
            if i in numone:
                return i
        return -1        