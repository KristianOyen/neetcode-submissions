class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            difference = target - nums[i]
            if difference in hm:
                j = hm[difference]
                return [j, i]
            hm[n] = i


                
    