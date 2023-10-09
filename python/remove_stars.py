class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str

        Runtime: 205 ms (Beats 99.80%)
        Memory: 16.3 MB (Beats 60.86%)
        """

        count = 0
        ans = deque()
        s = s[::-1] 

        for c in s:
            if c == '*':
                count+=1
            elif count:
                count-=1
            else:
                ans.appendleft(c) 

        return  ''.join(ans)
        
