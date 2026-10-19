class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_freq = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 in nums_freq:
                continue

            length = 1
            while num + 1 in nums_freq:
                length += 1
                num += 1

            if length > max_length:
                max_length = length

        return max_length