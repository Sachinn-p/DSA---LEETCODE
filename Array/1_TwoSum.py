class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for idx, val in enumerate(nums):
            num = target - val
            if val in hashMap:
                return [hashMap[val], idx]
            hashMap[num] = idx
        return []        