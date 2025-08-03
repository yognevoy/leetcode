class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        peak = False

        if length < 3:
            return False
        
        for i in range(length - 1):
            if arr[i + 1] > arr[i]:
                if peak != True:
                    continue
                else:
                    return False
            elif arr[i + 1] == arr[i]:
                return False
            else:
                if i == 0:
                    return False
                if peak != True:
                    peak = True

        return peak
