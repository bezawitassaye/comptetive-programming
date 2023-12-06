class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashset={}
        values=[]
        for i in nums:
            if i not in hashset:
                hashset[i]=1
            else:    
                hashset[i]+=1
        
        n=len(nums)//3
        for key in hashset:
            print(hashset)
            if hashset[key]>n:
                values.append(key)
        return values        
        
                   
        