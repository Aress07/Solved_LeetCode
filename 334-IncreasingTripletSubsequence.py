class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        l = len(nums)
        if l < 3:
            return False
        while i < j and j < l - 1:
            if nums[i] < nums[j]:
                break
            i += 1
            j += 1
        A = nums[i]
        B = nums[j]
        for c in range(j, l):
            C = nums[c] 
            if A < C and C < B:
                B = C
            elif C < A:
                A = C
            elif B < C:
                return True
        return False
        
