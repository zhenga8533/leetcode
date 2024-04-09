class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = tickets[k]

        for i in range(len(tickets)):
            if tickets[i] < n:
                time += tickets[i]
            elif i > k:
                time += n - 1
            else:
                time += n

        return time
