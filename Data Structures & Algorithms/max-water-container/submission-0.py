class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            current_area = (r - l) * min(heights[r], heights[l])

            if current_area > max_area:
                max_area = current_area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area