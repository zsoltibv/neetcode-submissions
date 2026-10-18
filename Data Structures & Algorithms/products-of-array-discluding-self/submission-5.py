class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        suffix = [1] * len(nums)

        prod, res = 1, []
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i] 

        prod, res = 1, []
        for i in range(len(nums)):            
            res.append(prod * suffix[i])
            prod *= nums[i]

        return res