class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0

        for i in range(len(nums)):
           if nums[i] != 0:
                nums[k] = nums[i]
                if k != i:
                    nums[i] = 0
                k += 1
