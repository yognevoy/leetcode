class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = 0
        expected = []
        count = [0] * (max(heights) + 1)
        
        for i in range(len(heights)):
            count[heights[i]] += 1

        for i in range(len(count)):
            for j in range(count[i]):
                expected.append(i)

        for i in range(len(heights)):
            if heights[i] != expected[i]:
                n += 1

        return n
