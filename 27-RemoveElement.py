class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        aux = []
        length = len(nums)
        count = 0

        for i in range(length):
            if (nums[i] != val):
                aux.append(nums[i])
                count += 1

        for i in range(len(aux)):
            nums[i] = aux[i]

        return count