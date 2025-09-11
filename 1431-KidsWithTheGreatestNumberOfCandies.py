class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        A = [[i for i in candies]]
        A.append([False for i in candies])

        for i in range(len(candies)):
            if A[0][i] + extraCandies >= max(A[0]):
                A[1][i] = True
        
        return A[1]
