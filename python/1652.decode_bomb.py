class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        ans = []
        key = 0

        dir = 1 if k > 0 else -1
        for i in range(dir, k + dir, dir):
            key += code[i]

        for i in range(n):
            ans.append(key)
            if k > 0:
                key -= code[(i + 1) % n]
                key += code[(i + k + 1) % n]
            else:
                key -= code[(i + k) % n]
                key += code[i]
        
        return ans
