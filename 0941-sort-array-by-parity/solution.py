class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k = 0

        for i in range(len(nums)):
           if nums[i] % 2 == 0:
                current = nums[k]
                nums[k] = nums[i]
                if k != i:
                    nums[i] = current
                k += 1
        
        return nums
