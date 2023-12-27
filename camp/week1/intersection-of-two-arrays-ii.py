class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                arr.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))    
        return arr        
        