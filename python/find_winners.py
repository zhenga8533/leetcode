class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)

        for match in matches:
            losses[match[1]] += 1
            if match[0] not in losses:
                losses[match[0]] = 0
        
        ans = [[], []]
        for p in sorted(losses.keys()):
            if losses[p] == 0:
                ans[0].append(p)
            elif losses[p] == 1:
                ans[1].append(p)
        
        return ans
