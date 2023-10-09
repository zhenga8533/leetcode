class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Runtime: 608 ms (Beats 10.67%)
        Memory: 23.5 MB (Beats 10.89%)
        """

        counter = defaultdict(int)
        co = 0
        for x in nums:
            comp = k - x
            if counter[comp]>0:
                counter[comp]-=1
                co+=1
            else:
                counter[x] +=1
            print(counter)
        return co
        
