class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            searched_value = target - nums[i]

            if searched_value in seen:
                return [seen[searched_value], i]

            seen[nums[i]] = i