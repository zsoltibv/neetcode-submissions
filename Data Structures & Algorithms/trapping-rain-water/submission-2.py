class Solution:
    def trap(self, height: list[int]) -> int:
        max_l, max_r, total = 0, 0, 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] > max_l:
                max_l = height[l]

            if height[r] > max_r:
                max_r = height[r]

            if max_l <= max_r: 
                l += 1
                total += max(0, max_l - height[l])
            else:
                r -= 1
                total += max(0, max_r - height[r])

        return total