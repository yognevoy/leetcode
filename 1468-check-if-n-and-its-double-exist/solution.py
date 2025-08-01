class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        values = {}

        for i in range(len(arr)):
            if arr[i] * 2 in values:
                return True
            elif (arr[i] % 2 == 0) and (arr[i] / 2 in values):
                return True
            values[arr[i]] = True

        return False
