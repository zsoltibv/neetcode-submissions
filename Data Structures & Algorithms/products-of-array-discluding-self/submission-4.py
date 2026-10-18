class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix = [1] * len(nums)

        prod, res = 1, []
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1] 
            suffix[i] = prod

        prod, res = 1, [suffix[0]]
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            res.append(prod * suffix[i])

        return res