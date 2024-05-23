class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]

        Runtime: 542 ms (Beats 52.73%)
        Memory: 15.1 MB (Beats 16.65%)
        """

        n = len(arr)
        if (n < 2):
            return [-1]

        ans = []
        mx = max(arr[1:])
        arr.append(-1)

        for i in range(1, n):
            ans.append(mx)
            if (arr[i] == mx):
                mx = max(arr[i + 1:])
        ans.append(-1)

        return ans
        
