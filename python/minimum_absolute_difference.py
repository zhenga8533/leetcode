class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        ans = []

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]

            if diff < min_diff:
                ans = [[arr[i], arr[i + 1]]]
                min_diff = diff
            elif diff == min_diff:
                ans.append([arr[i], arr[i + 1]])
        
        return ans
        
