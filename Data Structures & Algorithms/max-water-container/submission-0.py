class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = 0
        for l in range(len(heights)):
            for r in range(l+1, len(heights)):
                areas = max(areas, min(heights[l], heights[r]) * (r-l))
        
        return areas