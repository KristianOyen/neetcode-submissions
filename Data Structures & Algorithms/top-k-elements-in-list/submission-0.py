class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        
        return result