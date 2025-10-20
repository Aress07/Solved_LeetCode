class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        list = []

        list.append(nums[0])
        for k in range(len(nums) - 1):
            if (nums[k+1] != nums[i]):
                list.append(nums[k+1])
                i = k + 1
        
        for k in range(len(list)):
            nums[k] = list[k]
        return len(list)        
    
     