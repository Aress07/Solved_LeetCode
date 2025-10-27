class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        h = [[nums[_], _] for _ in range(len(nums))]
        
        for c in range(len(h)):
            h[c][1] = (h[c][1] + k) % len(nums)


        for c in range(len(h)):
            nums[h[c][1]] = h[c][0]