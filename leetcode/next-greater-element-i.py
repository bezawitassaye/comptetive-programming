class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hashset={}
        for i in range(len(nums2)):
            stack.append(nums2[i])
            for j in range(i+1,len(nums2)):
                
                if stack[-1] < nums2[j] :
                    n=stack.pop()
                    hashset[n] =nums2[j]
                    break
            if stack:
                stack.pop()
                hashset[nums2[i]]=-1
        return [hashset[k] for k in nums1]       
                       
                


        