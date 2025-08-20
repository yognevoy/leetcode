class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        squares = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                squares[i] = nums[l] ** 2
                l += 1
            else:
                squares[i] = nums[r] ** 2
                r -= 1

        return squares
