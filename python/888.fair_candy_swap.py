class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) / 2
        alice = set(aliceSizes)

        for b in bobSizes:
            a = diff + b
            if a in alice:
                return [a, b]
