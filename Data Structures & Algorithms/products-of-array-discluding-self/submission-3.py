class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix, prefix = [1] * len(nums), [1] * len(nums)

        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            suffix[i] = prod

        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1] 
            prefix[i] = prod
            
        res = []
        for a, b in zip(prefix, suffix):
            res.append(a * b)

        return res