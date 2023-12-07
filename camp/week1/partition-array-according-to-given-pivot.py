class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1=[]
        nums2=[]
        for i in nums:
            if i < pivot:
                nums1.append(i)
            elif i > pivot:
                nums2.append(i)
            else:
                nums2.insert(0,pivot)    
        return nums1+nums2            
        