class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        tmp = 0
        for num in nums:
            if num == 1:
                tmp += 1
                if tmp > max:
                    max = tmp
            else:
                tmp = 0
        return max
