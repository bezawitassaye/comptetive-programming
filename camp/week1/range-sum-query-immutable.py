class NumArray:

    def __init__(self, nums: List[int]):
        co=0
        self.num=[]
        for i in  nums:
            co+=i
            self.num.append(co)

    def sumRange(self, left: int, right: int) -> int:
        left=self.num[left-1] if left > 0 else 0
        right = self.num[right]
        return right-left
     


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)