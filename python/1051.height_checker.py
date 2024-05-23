class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        temp = sorted(heights)

        for i in range(len(heights)):
            if temp[i] != heights[i]:
                ans += 1

        return ans
