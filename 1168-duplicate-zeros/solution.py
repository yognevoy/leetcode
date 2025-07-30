class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        rest = 0
        length = len(arr)
        
        for i in range(length):
            if i >= length - rest:
                break
            if arr[i] == 0:
                if i == length - rest - 1:
                    arr[length - 1] = 0
                    length -= 1
                    break
                rest += 1

        for i in range(length - rest - 1, -1, -1):
            if arr[i] == 0:
                arr[i + rest] = arr[i]
                rest -= 1
                arr[i + rest] = arr[i]
            else:
                arr[i + rest] = arr[i]
