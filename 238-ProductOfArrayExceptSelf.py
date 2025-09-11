from numpy import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre = [1] * length
        post = [1] * length

        pre[0] = 1        
        for i in range(1, length):
            pre[i] = nums[i-1] * pre[i-1]

        post[length - 1] = 1        
        for i in range(length - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        res = [0] * length
        for i in range(length):
            res[i] = pre[i] * post[i]
        return res
