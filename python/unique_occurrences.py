class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool

        Runtime: 14 ms (Beats 92.80%)
        Memory: 13.5 MB (Beats 26.47%)
        """

        occ = defaultdict(int)
        
        for num in arr:
            occ[num] += 1
        
        values = list(occ.values())

        return len(values) == len(set(values))
        
