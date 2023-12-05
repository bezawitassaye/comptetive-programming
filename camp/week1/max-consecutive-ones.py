class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        s = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                print(count)
            elif nums[i] != 1:
                count = 0
            s.append(count)
                
        return max(list(set(s)))