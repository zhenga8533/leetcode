class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        k_pp = k + 1
        dp = [0] * k_pp

        for i in range(n - 1, -1, -1):
            current_max = 0
            end = min(n, i + k)

            for j in range(i, end):
                current_max = max(current_max, arr[j])
                part_max = dp[(j + 1) % k_pp] + current_max * (j - i + 1)
                dp[i % k_pp] = max(dp[i % k_pp], part_max)
        
        return dp[0]
