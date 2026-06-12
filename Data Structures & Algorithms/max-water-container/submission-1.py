class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1  # 左右指針
        max_area = 0  # 初始化最大水量

        while l < r:
            # 計算當前容器的容量
            current_area = min(heights[l], heights[r]) * (r - l)
            # 更新最大水量
            max_area = max(max_area, current_area)

            # 移動指針：移動較短的柱子指針
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
