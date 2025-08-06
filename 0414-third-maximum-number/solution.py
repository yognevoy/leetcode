class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        k = 0
        nums.sort(reverse=True)
        
        prev = nums[0]
        for i in range(len(nums)):
            if (i > 0 and nums[i] == prev):
                continue
            prev = nums[i]
            k += 1
            if k == 3:
                return nums[i]

        return nums[0]
