# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

class Solution:
    # Brute force method
    # Time complexity O(n^2), space complexity O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return nums.index()
        for i in range(0, n - 1):
            for j in range(i + 1, n - 1):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # Using Hashmap
    # Time complexity O(n), Space complexity O(n)
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]

            seen[value] = i
