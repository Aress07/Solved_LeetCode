class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashMap 
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
            if hashMap[i] > len(nums) / 2:
                return i