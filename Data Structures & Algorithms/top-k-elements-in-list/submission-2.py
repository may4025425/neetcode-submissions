class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ele_count = {}
        count = 0

        for i in nums:
            if i not in ele_count:
                count = 1
                ele_count[i] = count
            else:
                count = ele_count[i] + 1
                ele_count[i] = count
        
        return sorted(ele_count, key=ele_count.get, reverse=True)[:k]
            
        