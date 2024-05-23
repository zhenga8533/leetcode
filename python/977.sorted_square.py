class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = []
        ans = []

        # sort negatives from positive
        for num in nums:
            if num > 0:
                pos.append(num ** 2)
            elif num < 0:
                neg.append(num ** 2)
            else:
                ans.append(0)
        
        # add in increasing order
        p = len(pos)
        n = len(neg)
        while p != 0 and n != 0:
            if pos[0] > neg[n - 1]:
                ans.append(neg.pop())
                n -= 1
            else:
                ans.append(pos.popleft())
                p -= 1
        
        # add the rest
        if n != 0:
            ans.extend(neg[::-1])
        else:
            ans.extend(pos)
        
        return ans
