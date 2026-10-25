class Solution:
    def trap(self, height: list[int]) -> int:
        max_left, max_right = [], []
        max_val_left, max_val_right = 0, 0
        length = len(height)
        total_area = 0

        for i in range(length):
            max_left.append(max_val_left)

            if height[i] > max_val_left:
                max_val_left = height[i]

            max_right.append(max_val_right)

            if(height[length - 1 - i] > max_val_right):
                max_val_right = height[length - 1 - i]

        for i in range(length):
            current_area = min(max_left[i], max_right[length - 1 - i]) - height[i]
            if current_area < 0:
                current_area = 0

            total_area += current_area

        return total_area