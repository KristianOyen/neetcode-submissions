class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        while True:
            for i, n in enumerate(nums):
                difference = target - nums[i]
                if difference in seen: 
                    return [seen[difference], i]
                seen[n] = i

