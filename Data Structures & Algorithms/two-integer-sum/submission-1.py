class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}

        for i in range(len(nums)):
            searched_value = target - nums[i]
            searched: int = dict.get(searched_value, -1)

            if searched != -1:
                return [i, dict[searched_value]] if i < dict[searched_value] else [dict[searched_value], i]
            
            dict[nums[i]] = i

        return [0, 0]