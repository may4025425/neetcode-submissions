class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1

        for i, num in enumerate(nums):
            if num == target:
                return i
        