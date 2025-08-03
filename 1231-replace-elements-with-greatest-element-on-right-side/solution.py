class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        max = -1

        for i in range(length - 1, -1, -1):
            current = arr[i]
            arr[i] = max
            if current > max:
                max = current

        return arr

