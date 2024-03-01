class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sum_left = defaultdict(int)
        ct_left = defaultdict(int)
       

        for i ,x in enumerate(nums):
            res[i]+=ct_left[x] * i
            res[i]-=sum_left[x]
            ct_left[x]+=1
            sum_left[x]+=i
        sum_r = defaultdict(int)
        ct_r =  defaultdict(int)  

        for i,x in reversed(list(enumerate(nums))):
            res[i]+=sum_r[x]
            res[i]-=ct_r[x]*i

            ct_r[x]+=1
            sum_r[x]+=i
        return res    
    

    
        