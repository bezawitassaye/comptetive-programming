class NumArray:

    def __init__(self, nums: List[int]):
        
        self.output=[0]*len(nums)
        self.count=0
        for i in range(len(nums)):
            self.count+=nums[i]
            self.output[i]+=self.count
        print(self.output)    
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.output[right]
        return self.output[right]- self.output[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)