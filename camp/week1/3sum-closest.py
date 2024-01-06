class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the input list
        closest_sum = float('inf')  # Initialize the closest sum to infinity

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum  # Found an exact match, return the sum
                elif abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum  # Update the closest sum

                if current_sum < target:
                    left += 1  # Move the left pointer towards the right
                else:
                    right -= 1  # Move the right pointer towards the left

        return closest_sum