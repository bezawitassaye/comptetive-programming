class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_indices = {num: i for i, num in enumerate(nums)}
        for operation in operations:
            num_to_replace, replacement = operation
            index = num_indices[num_to_replace]
            nums[index] = replacement
            del num_indices[num_to_replace]
            num_indices[replacement] = index
        return nums